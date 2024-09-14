#!/usr/bin/python3

from lec.dummy_module import dummy_function, dummy_var
import rclpy
import yaml
from rclpy.node import Node


class Read(Node):
    def __init__(self):
        super().__init__('my_node')

        # Load the YAML file
        yaml_file_path = '/home/firm2204/exam1_ws/src/lec/yaml/params.yaml'
        self.load_parameters_from_yaml(yaml_file_path)

    def load_parameters_from_yaml(self, yaml_file_path):
        # Read the YAML file
        with open(yaml_file_path, 'r') as file:
            yaml_data = yaml.safe_load(file)

        # Extract the specific parameters for this node
        if 'my_node' in yaml_data and 'ros__parameters' in yaml_data['my_node']:
            parameters = yaml_data['my_node']['ros__parameters']

            # Get the nested_values parameter
            min_velocity = parameters.get('min_velocity', None)
            
            if min_velocity is not None:
                # Print the nested_values parameter
                self.get_logger().info(f"min_velocity: {min_velocity}")
            else:
                self.get_logger().info("nested_values parameter not found in YAML file")

def main(args=None):
    rclpy.init(args=args)
    node = Read()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
