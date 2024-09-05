#!/usr/bin/python3
import rospy
from sensor_msgs.msg import LaserScan
import math

pub = rospy.Publisher('/front/scan', LaserScan, queue_size=100)


def vicon_cb(msg):
    pub.publish(msg)

if __name__ == '__main__':
    rospy.init_node('remapscan')
    rospy.Subscriber('/scan', LaserScan, vicon_cb, queue_size=100)
    rospy.spin()

