import arcade


class Pan:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def update(self, delta):
        pass


class Circle:
    def __init__(self, world, x, y, vx, vy, r=20):
        self.world = world
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.r = r

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.x >= self.world.width - self.r:
            self.vx -= 1
        elif self.y >= self.world.height - self.r:
            self.vy -= 1
        elif self.x <= self.r:
            self.vx += 1
        elif self.y <= self.r:
            self.vy += 1

    def draw(self):
        arcade.draw_circle_outline(self.x, self.y, 20, arcade.color.WHITE)


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.pan = Pan(self, self.width // 4, self.height // 2)
        self.circle = Circle(self, self.width // 4, self.height // 3, 0, 0)

    def update(self, delta):
        self.pan.update(delta)
