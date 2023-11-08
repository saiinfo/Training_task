class Robot:
    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation

    def move_forward(self, distance):
        self.x += distance * math.cos(self.orientation)
        self.y += distance * math.sin(self.orientation)

    def turn_left(self, angle):
        self.orientation += angle

    def turn_right(self, angle):
        self.orientation -= angle

    def get_position(self):
        return (self.x, self.y)

    def get_orientation(self):
        return self.orientation
