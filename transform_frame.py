#!/usr/bin/env python3

import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped


def main():
    rospy.init_node('frame_transformation')

    broadcaster = tf2_ros.StaticTransformBroadcaster()
    transforms = []

    # Frame 1: base_scan is 0.20m above base_footprint
    t1 = TransformStamped()
    t1.header.stamp = rospy.Time.now()
    t1.header.frame_id = 'base_footprint'
    t1.child_frame_id = 'base_scan'
    t1.transform.translation.z = 0.20
    t1.transform.rotation.w = 1.0
    transforms.append(t1)

    # Frame 2: left_limit is 0.07m to the left of base_scan
    t2 = TransformStamped()
    t2.header.stamp = rospy.Time.now()
    t2.header.frame_id = 'base_scan'
    t2.child_frame_id = 'left_limit'
    t2.transform.translation.y = 0.07
    t2.transform.rotation.w = 1.0
    transforms.append(t2)

    # Frame 3: right_limit is 0.07m to the right of base_scan
    t3 = TransformStamped()
    t3.header.stamp = rospy.Time.now()
    t3.header.frame_id = 'base_scan'
    t3.child_frame_id = 'right_limit'
    t3.transform.translation.y = -0.07
    t3.transform.rotation.w = 1.0
    transforms.append(t3)

    broadcaster.sendTransform(transforms)
    rospy.loginfo('TF frames broadcast: base_scan, left_limit, right_limit')
    rospy.spin()


if __name__ == '__main__':
    main()
