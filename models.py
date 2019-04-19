import arcade
import math

# SCREEN_TITLE = "Bualoi"


class Pan:
    # TILT_ANGLE = 30
    # TILT_BACK = -15
    TILT_UP = 3
    TILT_DOWN = -1

    def __init__(self, world, x, y, angle, width):
        self.world = world
        self.x = x
        self.y = y
        self.angle = angle
        # self.height = height
        self.width = width
        self.ball = range(17, 39)
        self.ball = list(map(lambda x: x*10, self.ball))

    def tilt(self):
        self.angle += Pan.TILT_UP

    def update(self, delta):
        if self.world.spacebar_hold:
            if self.angle <= 15:
                self.angle += 2
        else:
            if self.angle <= -15:
                pass
            else:
                self.angle -= 1


# ning
        # if self.angle <= -15:
        #     pass
        # else:
        #     # self.angle -= 5
        #     self.angle -= 1


class Circle:
    GRAVITY = 0.01  # a
    STARTING_VELOCITY = 0.8  # a

    def __init__(self, world, x, y, dx, dy, r=20):
        self.world = world
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.angle = 0
        self.dy = Circle.STARTING_VELOCITY
        self.r = r

    # def hit(self, other, hit_size):
    #     return (abs(self.x - other.width) <= hit_size) and (abs(self.y - other.y) <= hit_size)

    def move(self):
        pass

        # self.y += self.dy
        # self.dy -= 0.5
        # self.dy -= Circle.GRAVITY

        # self.x += self.dx
        # self.y += self.dy

        # if self.x >= self.world.width - self.r:
        #     self.dx -= 1
        # elif self.y >= self.world.height - self.r:
        #     self.dy -= 1
        # elif self.x <= self.r:
        #     self.dx += 1
        # elif self.y <= self.r:
        #     self.dy += 1

    # def draw(self):
    #     # arcade.draw_circle_outline(self.x, self.y, 20, arcade.color.ORANGE_RED)
    #     arcade.draw_circle_filled(self.x, self.y, 20, arcade.color.BLACK)

    def update(self, delta, way):
        # if self.dy > 0 :
        #     self.dy -= 0.2

        if way == 0:
            # b
            temp_dx = self.dx
            temp_dy = self.dy
            if self.x >= self.world.width - self.r or self.x <= self.r or self.y <= self.r:
                self.dy = 0
                self.world.reset()
                # self.dx -= temp_dx
            # elif self.y >= self.world.height - self.r:
            #     self.dy -= temp_dy
                # self.dx = (-1)*temp_dx
                # self.dy = (-1)*temp_dy

            # elif self.x <= self.r:`
            #     self.dx += temp_dx
            # elif self.y <= self.r:
            #     self.dy += temp_dy
# b
            self.y += self.dy
            self.dy -= 0.5
            self.dy -= Circle.GRAVITY
            self.x -= self.dx

        elif way == 1:
            # เขียนโปรเจคไทล์ ตามมุมด้วยนะจ้ะ
            self.y += 20
            self.dy = 20
            self.y += self.dy

            # self.x += self.dx

            self.dx = self.world.pan.angle  # b
            self.x -= self.dx

            # if self.world.pan.angle < 0:
            #     self.dx += (-1)*self.world.pan.angle
            # elif self.world.pan.angle > 0:
            #     self.dx += self.world.pan.angle

            # if self.world.pan.angle


class World:
    STATE_FROZEN = 1  # a
    STATE_STARTED = 2  # a

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.pan = Pan(self, 50, 200, -15, 400)
        self.state = World.STATE_FROZEN  # a
        self.circle = Circle(self, 350, 700, 0, 0)

        self.spacebar_hold = False

    # def hit(self):
    #     return (self.circle.x <= self.pan.width) and self.circle.y <= self.pan.y

    def reset(self):
        # น่าจะพังตรงนี้ reset ไม่ได้#ได้และ
        self.circle.x = 350
        self.circle.y = 700
        self.circle.dx = 0
        self.dy = 0
        # self.circle.y = 0
        self.state = World.STATE_FROZEN  # a
        # self.circle = Circle(self, 350, 700, 0, 0)

    # def on_key_press(self, key, key_modifiers):
    #     self.pan.tilt()
    #     self.circle.move()

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.spacebar_hold = True

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.spacebar_hold = False

    def update(self, delta):
        if self.state == World.STATE_FROZEN:
            return
        # if (self.circle.x <= self.pan.width+30) and self.circle.y <= self.pan.y + 60:
        hit = False
        xc = self.circle.x
        yc = self.circle.y
        yc2 = self.circle.y - self.circle.dy

        for ball in self.pan.ball:
            # self.x + (ball * math.cos(angle/55)), self.y + (ball * math.sin(angle/55))+20
            x = self.pan.x + ball * math.cos(self.pan.angle/55)
            y = self.pan.y + ball * math.sin(self.pan.angle/55)+40
            r = 10
            if r**2 + 10 >= (x-xc)**2 + (y-yc)**2:
                hit = True
            if r**2 + 10 >= (x-xc)**2 + (y-yc2)**2:
                hit = True
        # print(self.pan.x + (ball * math.cos(self.pan.angle/55) ))
        if hit:
            self.circle.update(delta, 1)
        else:
            self.circle.update(delta, 0)
        self.pan.update(delta)
# a

    def start(self):
        self.state = World.STATE_STARTED

    def freeze(self):
        self.state = World.STATE_FROZEN

    def is_started(self):
        return self.state == World.STATE_STARTED
# a
