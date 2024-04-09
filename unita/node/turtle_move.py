#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist


rospy.init_node('turtle_move')
pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)

rate = rospy.Rate(10)

go = Twist()
go.linear.x = 3.0
go.angular.z = 3.0

while not rospy.is_shutdown():
    pub.publish(go)
    rate.sleep()


