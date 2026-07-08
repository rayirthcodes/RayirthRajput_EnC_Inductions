#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from kratos_rayirth_msgs.msg import RoverStatus


class RoverStatusSubscriber(Node):

    def __init__(self):
        super().__init__("rover_status_msg_subscriber")

        self.subscription = self.create_subscription(
            RoverStatus,
            "/rover_status",
            self.status_callback,
            10
        )

    def status_callback(self, msg):

        self.get_logger().info(
            f"Battery: {msg.battery_percentage} | "
            f"Velocity: {msg.velocity} | "
            f"Emergency: {msg.emergency_stop} | "
            f"Mode: {msg.mode}"
        )


def main(args=None):

    rclpy.init(args=args)

    node = RoverStatusSubscriber()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
