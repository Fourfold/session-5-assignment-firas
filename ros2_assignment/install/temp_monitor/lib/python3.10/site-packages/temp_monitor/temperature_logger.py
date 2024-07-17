import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import logging
import os

class TemperatureLogger(Node):
    def __init__(self):
        super().__init__('temperature_logger')
        self.subscriber = self.create_subscription(Int16, 'temperature', self.temperature_callback, 10)
        self.logger = logging.getLogger('temperature_logger')
        self.logger.setLevel(logging.INFO)
        log_file_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '..', '..', 'log', 'temperature_logs.log')
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def temperature_callback(self, tempMsg):
        temperature = tempMsg.data
        self.logger.info(f"Read temperature sensor data: {temperature}")

def main(args=None):
    rclpy.init(args=args)
    temperature_logger = TemperatureLogger()
    rclpy.spin(temperature_logger)
    temperature_logger.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()