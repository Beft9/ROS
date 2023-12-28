cmake_minimum_required(VERSION 3.0.2)
project(robot_localization)

find_package(catkin
  REQUIRED COMPONENTS
	hector_mapping
    sensor_msgs
)

catkin_package(
  CATKIN_DEPENDS
    sensor_msgs
)
