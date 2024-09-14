#!/usr/bin/python3

from lec.dummy_module import dummy_function, dummy_var
import rclpy
import yaml
import os
from rclpy.node import Node
from ament_index_python.packages import get_package_share_directory


class DummyNode(Node):
    def __init__(self):
        super().__init__('my_node')
        self.declare_parameter('max_velocity', 2.0)
        self.declare_parameter('min_velocity', 15.5)

    def save_parameters_to_yaml(self, file_path):
        # Get all parameters from the node
        parameters = self._parameters
        
        # Convert them to a dictionary
        param_dict = {name: param.value for name, param in parameters.items()}
        
        # Save to YAML file
        with open(file_path, 'w') as file:
            yaml.dump({'my_node': {'ros__parameters': param_dict}}, file)


def main(args=None):
    rclpy.init(args=args)
    node = DummyNode()
    yaml_file_path = '/home/firm2204/exam1_ws/src/lec/yaml/params.yaml'

    # Save parameters to the YAML file
    node.save_parameters_to_yaml(yaml_file_path)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
