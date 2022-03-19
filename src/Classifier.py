#!/usr/bin/env python
import rospy
import pickle
import numpy as np
from std_msgs.msg import String
from std_msgs.msg import Int32
from std_msgs.msg import Float64MultiArray
svm = pickle.load(open('/home/adel/work/src/bcinterface/src/svm_classifier.sav','rb'))
x=0
pub = rospy.Publisher('BCI_Command',Int32)

#global temp=-1
def callback(data):

    featureVector = np.array(data.data)
    rospy.loginfo("featureVectorzzz")
    rospy.loginfo(featureVector.shape)
    rospy.loginfo("******************")

    featureVector = featureVector.reshape(featureVector.shape[0],1)
    featureVector = np.transpose(featureVector)
    rospy.loginfo("featureVector")
    rospy.loginfo(featureVector.shape)
    rospy.loginfo("******************")

    label = svm.predict(featureVector)	
    rospy.loginfo("class")
    rospy.loginfo(label)
    rospy.loginfo("******************")
    pub.publish(label)
	
    

def listener():

    rospy.init_node('Classifier', anonymous=True)
    rospy.Subscriber('Final_Feature_vector', Float64MultiArray, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

#34210
