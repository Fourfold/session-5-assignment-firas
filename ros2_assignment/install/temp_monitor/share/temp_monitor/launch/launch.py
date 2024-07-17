from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='temp_monitor',
            executable='temperature_sensor',
            name='temperature_sensor'
        ),
        Node(
            package='temp_monitor',
            executable='temperature_alert',
            name='temperature_alert'
        ),
        Node(
            package='temp_monitor',
            executable='alert',
            name='alert'
        )
    ])