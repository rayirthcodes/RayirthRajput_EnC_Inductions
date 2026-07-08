#!/usr/bin/env python3
import rclpy

from rclpy.node import Node

from std_msgs.msg import Float32, String, Bool


class RoverStatusPublisher(Node):

    def __init__(self):
        super().__init__("rover_status_publisher")

        self.battery_publisher = self.create_publisher(
            Float32,
            "/battery_level",
            10
        )
        
        self.mode_publisher = self.create_publisher(
            String,
            "/rover_mode",
            10
        )

        self.emergency_publisher = self.create_publisher(
            Bool,
            "/emergency_stop",
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_status
        )

        self.battery = 100.0
        self.mode = "AUTONOMOUS"
        self.emergency = False
        
    def publish_status(self):

        battery_msg = Float32()
        battery_msg.data = self.battery

        mode_msg = String()
        mode_msg.data = self.mode

        emergency_msg = Bool()
        emergency_msg.data = self.emergency

        self.battery_publisher.publish(battery_msg)
        self.mode_publisher.publish(mode_msg)
        self.emergency_publisher.publish(emergency_msg)

        self.get_logger().info(
            f"Battery: {self.battery} | Mode: {self.mode} | Emergency: {self.emergency}"
        )
def main(args=None):
    rclpy.init(args=args)

    node = RoverStatusPublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
