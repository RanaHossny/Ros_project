#!/usr/bin/env python3
import rospy
import math
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
cmd=Twist()
def pose_callback(pose:Pose):
    x_goal=3
    y_goal=3
    dif_x=x_goal-pose.x
    dif_y=y_goal-pose.y
    Beta=rospy.get_param("/Beta")
    Alpha=rospy.get_param("/Alpha")
    cmd.linear.x=Beta*math.sqrt(pow(dif_x,2)+pow(dif_y,2))
    cmd.angular.z=(Alpha*((-1*pose.theta)+(math.atan2(dif_y,dif_x))))
    if (cmd.angular.z<=0.01 and cmd.linear.x>=x_goal-0.01 and  cmd.linear.x<=x_goal+0.01):
        cmd.linear.x=0
        cmd.angular.z=0     
    pub.publish(cmd)


rospy.init_node('controller_node')
rospy.loginfo('hello from controller_node')
pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
rospy.Subscriber('/turtle1/pose',Pose,callback=pose_callback)
rospy.loginfo('the node has been started')
rospy.spin()