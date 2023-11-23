class DroneNode:
    def __init__(self, identifier):
        self.identifier = identifier
        self.left_child = None
        self.right_child = None

def create_binary_tree():
    root = DroneNode(1)
    drone2 = DroneNode(2)
    drone3 = DroneNode(3)
    drone4 = DroneNode(4)
    drone5 = DroneNode(5)
    drone6 = DroneNode(6)
    drone7 = DroneNode(7)
    drone8 = DroneNode(8)

    root.left_child = drone2
    root.right_child = drone3

    drone2.left_child = drone4
    drone2.right_child = drone5

    drone3.left_child = drone6

    drone6.left_child = drone7
    drone6.right_child = drone8

    return root

def synchronize_drones(node):
    if node is not None:
        print(f"Synchronizing drones {node.identifier}")
        synchronize_drones(node.left_child)
        synchronize_drones(node.right_child)

root_drone = create_binary_tree()
synchronize_drones(root_drone)
