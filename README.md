# Robotics Assignment - Session 5 - ROS2

To build the project, enter the following commands while in the directory of the repository:
```
cd ros2_assignment
source install/setup.bash
colcon build
```
---
Then, to run the project, enter:
```
cd src/temp_monitor/launch
ros2 launch launch.py
```
---
After the project is run, you can enter the following commands on another terminal in the repository to view the alerts being published:
```
cd ros2_assignment
source install/setup.bash
ros2 topic echo alert
```
---
Finally, to view the logs of the temperature logger node, you can find the logs file in the following path: `ros2_assignment/log/temperature_logs.log`
