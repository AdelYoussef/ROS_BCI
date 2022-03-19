#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64MultiArray
import numpy
import pickle
from scipy import signal
Feature_vector = Float64MultiArray()
pub = rospy.Publisher('Final_Feature_vector', Float64MultiArray, queue_size=10)
pca = pickle.load(open('/home/adel/work/src/bcinterface/src/PCA.sav','rb'))

def callback(data):

    Features = numpy.array(data.data)
    Features = Features.reshape(Features.shape[0],1)
    Features = numpy.transpose(Features)
    #rospy.loginfo("pca shape")
    #rospy.loginfo(Features.shape)
   # rospy.loginfo("**********************")
    featureVector = pca.transform(Features)
    rospy.loginfo("pca output")
    rospy.loginfo(featureVector.shape)
    rospy.loginfo("**********************")
    featureVector = numpy.transpose(featureVector)
    rospy.loginfo(featureVector.shape)
    Feature_vector.data=featureVector[:,0]

    pub.publish(Feature_vector)
    
def listener():

    rospy.init_node('PCA', anonymous=True)
    rospy.Subscriber('Feature_vector', Float64MultiArray, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
