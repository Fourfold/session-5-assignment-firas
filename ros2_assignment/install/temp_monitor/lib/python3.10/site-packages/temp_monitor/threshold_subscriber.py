import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
from std_msgs.msg import Bool

class ThresholdSubscriber(Node):
    def __init__(self):
        super().__init__('temperature_alert')
        self.publisher = self.create_publisher(Bool, 'alert_trigger', 10)
        self.subscriber = self.create_subscription(Int16, 'temperature', self.temperature_callback, 10)
        self.threshold = 25

    def temperature_callback(self, tempMsg):
        if (tempMsg.data > self.threshold):
            alertMsg = Bool()
            alertMsg.data = True
            self.publisher.publish(alertMsg)

def main(args=None):
    rclpy.init(args=args)
    temperature_alert = ThresholdSubscriber()
    rclpy.spin(temperature_alert)
    temperature_alert.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
        
