#!/usr/bin/env python

import rospy
import sys
import cv2
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge, CvBridgeError


class Bridge():
    def __init__(self, callback, topic, resize=1.0):
        self.node_name = "cv_brige"

        rospy.init_node(self.node_name)

        rospy.on_shutdown(self.cleanup)

        self.briger = CvBridge()

        self.resize = resize

        self.callback = callback

        self.depth_sub = rospy.Subscriber(
            topic, Image, self.depth_callback, queue_size=1)

        rospy.loginfo("Waiting...")

    def depth_callback(self, ros_image):
        try:            
            depth_image = self.briger.imgmsg_to_cv2(
                ros_image, desired_encoding="passthrough")
            depth_image = cv2.resize(
                depth_image, (0, 0), fx=self.resize, fy=self.resize)
            self.callback(depth_image)
        except CvBridgeError, e:
            rospy.logerr(e)
            rospy.signal_shutdown(e)

    def cleanup(self):
        print "Shutting down vision node."