#!/usr/bin/python3

from lec.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node
import yaml

class DummyNode(Node):
    def __init__(self):
        super().__init__('dummy_node')
        self.get_logger().info('Parameters loaded from YAML file')
        self.declare_parameter('max_velocity', 2.0)
        self.declare_parameter('min_velocity', 10.5)

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
    node.save_parameters_to_yaml('params.yaml')
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
