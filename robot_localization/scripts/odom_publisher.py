#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from std_msgs.msg import Header
from nav_msgs.msg import Odometry

class odom_publisher:
    def __init__(self):
        rospy.init_node('odom_publisher')

        # Subscribe to ropot position published by hector mapping
        rospy.Subscriber('/poseupdate', PoseWithCovarianceStamped, self.pose_callback)

        # Publisher for reported position and orientation
        self.odom_publisher = rospy.Publisher('/odom', Odometry, queue_size=10)

    
    def pose_callback(self, pose):
        # Report position and orientation to /robot/odom
        self.curr_pos = pose.pose.pose
        odom = Odometry()
        odom.header.stamp = rospy.Time.now()
        odom.header.frame_id = "map"
        odom.child_frame_id = "base_link"
        odom.pose = pose.pose
        self.odom_publisher.publish(odom)

if __name__ == '__main__':
    try:
        task=odom_publisher()
        rospy.spin()

    except rospy.ROSInterruptException:
        pass
