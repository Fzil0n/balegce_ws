#!/usr/bin/python3

from balegce_gazebo.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
import math

class DummyNode(Node):
    def __init__(self):
        super().__init__('read_imu_node')
        self.eulerAngles = [0, 0, 0]
        # create subscriber
        self.sub_imu = self.create_subscription(Imu,"/imu",self.imu_callback,10)
        # create publish
        self.pub_euler = self.create_publisher()
    # class's method
    def imu_callback(self,msg):
        pass


def main(args=None):
    rclpy.init(args=args)
    node = DummyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
