#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64MultiArray
import numpy as np
from scipy import signal

epocksize=750
windowsize = 750
overlap = 0     #Percentage overlap of windows

n=int(((epocksize-windowsize)/((1-overlap)*windowsize))+1) #Number of loops in for loop to concatenate features of windows
increment = int((1-overlap)*windowsize)                    #Number of samples to be incremented every window

nperseg = 600    #number of samples per welch segment
noverlap =550
fs = 250

Feature_vector = Float64MultiArray()
pub = rospy.Publisher('Feature_vector', Float64MultiArray, queue_size=10)

def callback(data):
    Filtered = np.array(data.data)
    for i in range(n):
        freq0, freq0_welch = signal.welch(Filtered[(i*increment):(windowsize+(i*increment))], fs, nperseg=nperseg, noverlap=noverlap, nfft=nperseg, axis =0)
	if i==0:
	   features=freq0_welch
	else:
	   features=np.concatenate((class0_features,freq0_welch), axis = 0)
    Feature_vector.data= features
    rospy.loginfo("feature vector")
    rospy.loginfo(Feature_vector.data.shape)
    rospy.loginfo("************")
    pub.publish(Feature_vector)
    
def listener():
    rospy.init_node('PCA', anonymous=True)
    rospy.Subscriber('filtered_data', Float64MultiArray, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
