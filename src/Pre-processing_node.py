#!/usr/bin/env python

import rospy
import numpy
from std_msgs.msg import String
from std_msgs.msg import Float64MultiArray
from scipy.signal import butter, lfilter
from scipy import signal
import preprocessing

window_size = 500
sent = Float64MultiArray()
pub = rospy.Publisher('filtered_data', Float64MultiArray, queue_size=10)

fs = 250      #Sampling Frequency of OpenBCI
lowcut = 8     #Low Frequency
highcut = 60  #High Frequency
order = 2       #Order of Butterworth Filter

f0 = 50
bw = 3

def butter_bandpass(lowcut, highcut, fs, order):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def iir_notch(f0, bw, fs):
    nyq = 0.5 * fs
    f = f0 / nyq
    Q = f0/bw
    b, a = signal.iirnotch(f, Q)
    return b, a

b, a = butter_bandpass(lowcut, highcut, fs, order) #b, a are properties of filter
c, d = iir_notch(f0, bw, fs)


def callback(data):
    EEGdata = numpy.array(data.data)                   # Put data in numpy array
    #rospy.loginfo("eegrawshape")
    #rospy.loginfo(EEGdata.shape)                       # show shape of data
    #rospy.loginfo("***************")
    EEGdata-= EEGdata.mean(axis=0, keepdims=1)         # remove mean from data
    filtered_Data =lfilter(b, a, EEGdata, axis=0)      # band-pass filter  
    filtered_Data =lfilter(c, d, filtered_Data, axis=0)# notch filter 50hz
    sent.data = filtered_Data
    pub.publish(sent)                                  # Send filtered data to next node

def listener():
    rospy.init_node('preprocessing', anonymous=True)
    rospy.Subscriber('epoched_data', Float64MultiArray, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

