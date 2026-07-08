#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String, Bool


class RoverStatusSubscriber(Node):

    def __init__(self):
        super().__init__("rover_status_subscriber")

        self.create_subscription(
            Float32,
            "/battery_level",
            self.battery_callback,
            10
        )

        self.create_subscription(
            String,
            "/rover_mode",
            self.mode_callback,
            10
        )

        self.create_subscription(
            Bool,
            "/emergency_stop",
            self.emergency_callback,
            10
        )

    def battery_callback(self, msg):
        self.get_logger().info(f"Battery: {msg.data}")

    def mode_callback(self, msg):
        self.get_logger().info(f"Mode: {msg.data}")

    def emergency_callback(self, msg):
        self.get_logger().info(f"Emergency: {msg.data}")


def main(args=None):
    rclpy.init(args=args)

    node = RoverStatusSubscriber()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
