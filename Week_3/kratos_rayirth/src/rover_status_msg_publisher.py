#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from kratos_rayirth_msgs.msg import RoverStatus


class RoverStatusPublisher(Node):

    def __init__(self):
        super().__init__("rover_status_msg_publisher")

        self.publisher = self.create_publisher(
            RoverStatus,
            "/rover_status",
            10
        )

        self.timer = self.create_timer(
            0.5,
            self.publish_status
        )

        self.battery = 100.0
        self.velocity = 2.5
        self.emergency = False
        self.mode = "AUTONOMOUS"

    def publish_status(self):

        msg = RoverStatus()

        msg.battery_percentage = self.battery
        msg.velocity = self.velocity
        msg.emergency_stop = self.emergency
        msg.mode = self.mode

        self.publisher.publish(msg)

        self.get_logger().info(
            f"Battery: {msg.battery_percentage} | "
            f"Velocity: {msg.velocity} | "
            f"Emergency: {msg.emergency_stop} | "
            f"Mode: {msg.mode}"
        )


def main(args=None):

    rclpy.init(args=args)

    node = RoverStatusPublisher()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
