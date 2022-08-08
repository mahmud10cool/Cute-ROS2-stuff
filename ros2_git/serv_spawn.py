import rclpy
from rclpy.node import Node
from example_interfaces.srv import* 
from turtlesim.srv import*

class SpawnServer(Node):
    def __init__(self):
        super().__init__('spawn_server')

        self.create_service(Spawn, 'spawner', self.callback)

    def callback(self, request, response):
        request.x = 3
        request.y = 5
        request.theta = 3.14159
        
        response.name = 'Cutie Turtle'

        return response
    
def main(args=None):
    rclpy.init(args=args)
    node = SpawnServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()