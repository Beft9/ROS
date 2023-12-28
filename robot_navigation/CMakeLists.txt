cmake_minimum_required(VERSION 2.8.3)
project(robot_navigation)

find_package(catkin
  REQUIRED COMPONENTS
    move_base
    rospy
    nav_msgs
    geometry_msgs
    dynamic_reconfigure
)

generate_dynamic_reconfigure_options(
	 cfg/EnableWaypoints.cfg
 )

catkin_package(
  CATKIN_DEPENDS
    rospy
    nav_msgs
    geometry_msgs
)
