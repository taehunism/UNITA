#!/usr/bin/env python3

import rospy
import random
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def pose_callback(data):
    go = Twist()

    if 1.5 < data.x < 9.5 and 1.5 < data.y < 9.5:
        go.linear.x = random.uniform(1.0,2.0)
        go.angular.z = random.uniform(-1.5,1.5)
    else:
        go.linear.x = 1.0
        go.angular.z = 1.5

    pub.publish(go)

rospy.init_node('dont_touch_wall')

pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)

sub = rospy.Subscriber('turtle1/pose', Pose, pose_callback)
rate = rospy.Rate(10)

while not rospy.is_shutdown():

    rate.sleep()
