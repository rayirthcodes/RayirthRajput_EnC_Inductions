#!/usr/bin/env python3

import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64MultiArray


class DoubleAckermannController(Node):

    def __init__(self):
        super().__init__('double_ackermann_controller')

        self.cmd_sub = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_callback,
            10
        )

        self.steer_pub = self.create_publisher(
            Float64MultiArray,
            '/steering_controller/commands',
            10
        )

        self.drive_pub = self.create_publisher(
            Float64MultiArray,
            '/drive_controller/commands',
            10
        )

        self.wheelbase = 0.5
        self.track_width = 0.3
        self.wheel_radius = 0.12

        self.get_logger().info("Double Ackermann Controller Started")

    def cmd_callback(self, msg):

        linear_x = msg.linear.x
        angular_z = msg.angular.z

        # Straight driving
        if abs(angular_z) < 1e-6:

            fl_angle = 0.0
            fr_angle = 0.0
            rl_angle = 0.0
            rr_angle = 0.0

            wheel_speed = linear_x / self.wheel_radius

            fl_vel = wheel_speed
            fr_vel = wheel_speed
            rl_vel = wheel_speed
            rr_vel = wheel_speed

        else:

            L = self.wheelbase
            W = self.track_width
            R = linear_x / angular_z

            fl_angle = math.atan(L / (R - W/2))
            fr_angle = math.atan(L / (R + W/2))
            rl_angle = -fl_angle
            rr_angle = -fr_angle

            r_fl = math.sqrt((R - W/2)**2 + L**2)
            r_fr = math.sqrt((R + W/2)**2 + L**2)
            r_rl = math.sqrt((R - W/2)**2 + L**2)
            r_rr = math.sqrt((R + W/2)**2 + L**2)

            fl_vel = angular_z * r_fl / self.wheel_radius
            fr_vel = angular_z * r_fr / self.wheel_radius
            rl_vel = angular_z * r_rl / self.wheel_radius
            rr_vel = angular_z * r_rr / self.wheel_radius

        steer_msg = Float64MultiArray()
        steer_msg.data = [
            fl_angle,
            fr_angle,
            rl_angle,
            rr_angle
        ]
        self.steer_pub.publish(steer_msg)

        drive_msg = Float64MultiArray()
        drive_msg.data = [
            fl_vel,
            fr_vel,
            rl_vel,
            rr_vel
        ]
        self.drive_pub.publish(drive_msg)


def main(args=None):
    rclpy.init(args=args)

    node = DoubleAckermannController()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
