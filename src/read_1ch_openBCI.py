#!/usr/bin/env python

# import sys; sys.path.append('..') # help python find open_bci_v3.py relative to scripts folder
import open_bci_v3 as bci
import matplotlib.pyplot as plt # for plot
import collections # circular buffer
from time import sleep # sleep functions
from threading import Thread

# Ros packages:
import rospy
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Float64

# Gets data from one channel of OpenBci and plots the data in real time.
# Author: Rafael Duarte

# Global variables
i = 0
fa = 250 # sample frequency (approx)


def get_data(sample):
    # int64[2] data
    msg = Float64MultiArray()
    #msg.data = [rospy.get_time(), sample.channel_data]
    msg.data = [sample.channel_data]
    # print data
    msg2= Float64MultiArray()
    msg2.data= msg.data[0]	
    #rospy.loginfo(msg.data[0])
    pub.publish(msg2)


# Main loop
if __name__ == '__main__': # this code is only executed if this module is not imported
    # Channel which will be plotted
    channel = 8; 

    # Ros config:
    pub = rospy.Publisher('eeg_data', Float64MultiArray, queue_size=10)
    # pub_time = rospy.Publisher('time', Int64, queue_size=10)

    rospy.init_node('acquiring_data', anonymous=True)
    rate = rospy.Rate(250) # 10hz

    # OpenBCI config
    port = '/dev/ttyUSB0' # port which opnbci is connected (linux). windows = COM1
    baud = 115200
    board = bci.OpenBCIBoard(port=port, baud=baud)
    board.test_signal(3)  # square waveform to channel input (test signal)
    sleep(1)              # need to include this to wait for test config setup

    board.start_streaming(get_data) # start getting data from amplifier
	
