Taken from https://github.com/robotics/open_abb. All credits to them.


# open-abb-driver
### Control ABB robots remotely with Python

## Requirements
* ABB IRC5 controller
* 6 DOF robotic manipulator
* Robot must have the following factory software options
    * "PC Interface"
    * "Multitasking" (required for position feedback stream)

## Quick Start
### Robot Setup
* Install the RAPID module 'SERVER'
    * Using RobotStudio online mode is the easiest way to do this, check out the [wiki article](https://github.com/robotics/open-abb-driver/wiki/Configuring-an-ABB-Robot-for-OAD) for details.
* For position feedback, install the RAPID module 'LOGGER' into another task. 
* In SERVER.mod, check to make sure the "ipController" specified is the same as your robot. The default robot IP is 192.168.125.1
* Start the programs on the robot
    * Production Window->PP to Main, then press the play button. 

### Computer Setup
* Verify that your computer is on the same subnet as the robot.
    * Try pinging the robot (default IP is 192.168.125.1). 
* Before trying ROS, it's pretty easy to check functionality using the [simple python interface.](https://github.com/robotics/open-abb-driver/wiki/Python-Control)

