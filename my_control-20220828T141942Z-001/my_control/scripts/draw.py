#!/usr/bin/env python3
from time import sleep
import rospy
from geometry_msgs.msg import Twist
if __name__=='__main__':
    rospy.init_node('draw_node')
    rospy.loginfo('hello from draw_node')
    pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        mag=Twist()
        mag.linear.x=4
        mag.angular.z=2
        pub.publish(mag)
        rate.sleep()