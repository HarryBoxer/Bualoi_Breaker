class Hand:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
 
    def update(self, delta):
        pass
 
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.hand = Hand(self, width // 4, height // 3)
 
    def update(self, delta):
        self.hand.update(delta)