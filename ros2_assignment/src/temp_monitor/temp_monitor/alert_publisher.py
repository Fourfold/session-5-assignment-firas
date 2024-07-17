import rclpi
from rclpi.node import Node
from std_msgs.msg import String
from std_msgs.msg import Bool

class AlertPublisher(Node):
    def __init__(self):
        super().__init__('alert')
        self.create_publisher(String, 'alert', 10)
        self.create_subscription(Bool, 'alert_trigger', self.alert_callback, 10)
    
    def alert_callback(self, triggerMsg):
        if (triggerMsg.data):
            alertMsg = String()
            alertMsg.data = "Alert: temperature exceeded!"
            self.publisher.publish(alertMsg)

def main(args=None):
    rclpy.init(args=args)
    alert = AlertPublisher()
    rclpy.spin(alert)
    alert.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()