import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/fourfold/dev/inmind sessions/inmind-session-5/session-5-assignment-firas/ros2_assignment/install/temp_monitor'
