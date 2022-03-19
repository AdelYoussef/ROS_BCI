#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64MultiArray
import numpy
window_size = 750
overlap = int(0*window_size)
i = -1  # counter to 50
flag = 0  # Flag that code reached one window
increament = window_size - overlap
counter = increament
pub = rospy.Publisher('epoched_data', Float64MultiArray, queue_size=10)
sent = Float64MultiArray()
def callback(data):
    global i
    global flag
    global counter
    #rospy.loginfo(i)
    if i < (window_size - 1):# check whether or not i reached the end of window 
        i = i+1 #increament to next cell
    else:
        i = 0 #new window

    if i==(window_size - 1): #thus, i reched one complete window (useless after the first 50 cells)
	flag=1
    mybuffer[:, i] = data.data # save every fifty samples in buffer 
    #rospy.loginfo(mybuffer)
    if flag == 1 and counter < increament:# increament counter and as it reached overlap size (increament variable) ;) it tends to save new window in the next few lines
        counter = counter + 1
    if flag == 1 and counter == increament:# start to save window and send it 
        if i < (window_size - 1): # buffer doesn't a complete window
            window[:, 0: (window_size - 1)-i] = mybuffer[:, i+1: window_size] # this two lines to put the buffer array in the window array (don't try to understand them again they are right)
        window[:, (window_size - 1)-i: window_size] = mybuffer[:, 0: i+1]
        counter = 0 
        sent.data= window[1, 0:window_size]
	pub.publish(sent)
        #rospy.loginfo(window.shape)
        #rospy.loginfo("//////////////////////")
        #rospy.loginfo(sent.data)
        #rospy.loginfo("//////////////////////")


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'talker' node so that multiple talkers can
    # run simultaneously.
    rospy.init_node('epoching', anonymous=True)

    rospy.Subscriber('eeg_data', Float64MultiArray, callback)
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    mybuffer = numpy.array([[0.0] * window_size for i in range(8)])  # initialize array 8 rows and (window size) columns
    window = numpy.array([[0.0] * window_size for i in range(8)])    # initialize array 8 rows and (window size) columns
    i = -1
    flag = 0
    counter = increament
    listener()
