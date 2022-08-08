import rclpy
from rclpy.node import Node
from example_interfaces.srv import* 
from turtle import*
from turtlesim.srv import*
from turtlesim.msg import*
from functools import*

class SpawnServer(Node):
    def __init__(self):
        super().__init__('spawn_server')

        self.create_service(Spawn, 'spawner', self.callback)

        self.get_logger().info('Service has started.')

    def callback(self, request, response):
        request.x 
        request.y
        request.theta
        request.name

        response.name = request.name
        
        self.get_logger().info('The name of the new turtle is ' + response.name)

        return response
    
def main(args=None):
    rclpy.init(args=args)
    node = SpawnServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()