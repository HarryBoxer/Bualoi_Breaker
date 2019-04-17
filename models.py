import arcade

# SCREEN_TITLE = "Bualoi"



class Pan:
    TILT_ANGLE = 30
    TILT_BACK = -15

    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y
        self.angle = angle
        # self.angle = -5

    def tilt(self):
        self.angle = Pan.TILT_ANGLE
        # self.angle = Pan.TILT_BACK

    def update(self, delta):
        if self.angle < -15:
            pass
        else:
            self.angle -= 5


class Circle:
    # GRAVITY = 0.5 #a
    # STARTING_VELOCITY = 9.8 #a

    def __init__(self, world, x, y, vx, vy, r=20):
        self.world = world
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = 9.8
        # self.vy = Circle.STARTING_VELOCITY
        self.r = r

    def move(self):
        # self.y += self.vy
        # self.vy -= 0.5
        # self.vy -= Circle.GRAVITY

        self.x += self.vx
        self.y += self.vy

        # if self.x >= self.world.width - self.r:
        #     self.vx -= 1
        # elif self.y >= self.world.height - self.r:
        #     self.vy -= 1
        # elif self.x <= self.r:
        #     self.vx += 1
        # elif self.y <= self.r:
        #     self.vy += 1

    # def draw(self):
    #     # arcade.draw_circle_outline(self.x, self.y, 20, arcade.color.ORANGE_RED)
    #     arcade.draw_circle_filled(self.x, self.y, 20, arcade.color.BLACK)
    
    # def update(self, delta):
    #     self.y += self.vy
    #     self.vy -= 0.5
    #     self.vy -= Circle.GRAVITY


class World:
    # STATE_FROZEN = 1#a
    # STATE_STARTED = 2#a
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # self.state = World.STATE_FROZEN #a
        self.pan = Pan(self, 50, 200, -15)
        self.circle = Circle(self, 350, 700, 0, 0)

    def on_key_press(self, key, key_modifiers):
        self.pan.tilt()

    def update(self, delta):
        self.pan.update(delta)
#a
    # def start(self):
    #     self.state = World.STATE_STARTED

    # def freeze(self):
    #     self.state = World.STATE_FROZEN     

    # def is_started(self):
    #     return self.state == World.STATE_STARTED
#a

