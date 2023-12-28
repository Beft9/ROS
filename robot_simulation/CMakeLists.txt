cmake_minimum_required(VERSION 2.8.3)
project(robot_simulation)

find_package(catkin
  REQUIRED COMPONENTS
    gazebo_ros
)

catkin_package(
  CATKIN_DEPENDS
    rospy
    gazebo_ros
)
