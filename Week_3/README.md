# Week 3 - ROS2 Basics Assignment

## Overview

This repository contains solutions for the Week 3 ROS2 Basics assignment as part of the Kratos Electronics and Controls Inductions.

The assignment covers:

- ROS2 publishers and subscribers
- ROS2 topics
- Custom ROS2 message creation
- Message publishing and subscribing
- ROS2 command line tools

---

# Question 1

## Approach

I created a ROS2 package named `kratos_rayirth`.

Inside this package, I implemented:

- A publisher node that publishes:
  - Battery level
  - Rover mode
  - Emergency stop status

- A subscriber node that subscribes to all three topics and prints the received values.

I also verified the nodes using the ROS2 CLI commands:

- ros2 node list
- ros2 topic list
- ros2 topic type
- ros2 topic echo

Screenshots of all commands are included in the `assets` folder.

---

# Question 2

## Approach

I created a separate package called `kratos_rayirth_msgs` for defining a custom ROS2 message.

The custom message `RoverStatus.msg` contains:

- battery_percentage (float32)
- velocity (float32)
- emergency_stop (bool)
- mode (string)

I then created:

- A publisher node that publishes the custom RoverStatus message at 2 Hz.
- A subscriber node that receives the message and prints all the fields.

The message definition was verified using:

```
ros2 interface show kratos_rayirth_msgs/msg/RoverStatus
```

The topic was also verified using:

```
ros2 topic list
ros2 topic type
ros2 topic echo
```

---

# Assumptions
- The workspace has been sourced before running the nodes.

---

# Challenges Encountered

- Understanding the ROS2 package structure.
- Configuring package.xml and CMakeLists.txt correctly for custom messages.
- Setting executable permissions for Python nodes.
- Debugging package build errors and executable path issues.

---

# Testing

The implementation was tested using:

- colcon build
- ros2 run
- ros2 node list
- ros2 topic list
- ros2 topic type
- ros2 topic echo
- ros2 interface show

Both publisher and subscriber nodes were run simultaneously and verified to exchange messages correctly.

---

# Known Limitations

- Message values are currently hardcoded.
- No user input or dynamic rover data is used.
- The optional launch file was not implemented.

---

# Repository Structure

```
kratos_rayirth/
├── assets/
├── src/
├── CMakeLists.txt
├── package.xml

kratos_rayirth_msgs/
├── msg/
│   └── RoverStatus.msg
├── CMakeLists.txt
├── package.xml
```

---# RayirthRajput_EnC_Inductions
