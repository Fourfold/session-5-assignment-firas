import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import random

class TemperaturePublisher(Node):
    def __init__(self):
        super().__init__('temperature_sensor')
        self.publisher = self.create_publisher(Int16, 'temperature', 10)
        time_period = 1
        self.timer = self.create_timer(time_period, self.timer_callback)
    
    def timer_callback(self):
        temperature = random.randint(0,50)
        msg = Int16()
        msg.data = temperature
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    temperature_sensor = TemperaturePublisher()
    rclpy.spin(temperature_sensor)
    temperature_sensor.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()