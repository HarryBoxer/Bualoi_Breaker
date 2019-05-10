import arcade
import math
import os
from random import randint

SCEEN_TITLE = "Bualoi"


class Pan:
    TILT_UP = 3
    TILT_DOWN = -1

    def __init__(self, world, x, y, angle, width):
        self.world = world
        self.x = x
        self.y = y
        self.angle = angle
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

class Circle:
    GRAVITY = 0.01
    STARTING_VELOCITY = 0.8

    def __init__(self, world, x, y, dx, dy, r=20):
        self.world = world
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.angle = 0
        self.dy = Circle.STARTING_VELOCITY
        self.r = r


    def move(self):
        pass

    def update(self, delta, way):

        if way == 0:
            
            temp_dx = self.dx
            temp_dy = self.dy
            if self.x >= self.world.width - self.r:
                self.dx = -1*(temp_dx)

            if self.x <= self.r or self.y <= self.r:
                self.dy = 0
                self.world.reset()

            self.y += self.dy
            self.dy -= 0.5
            self.dy -= Circle.GRAVITY
            self.x -= self.dx

        elif way == 1:
            self.y += 20
            self.dy = 20
            self.y += self.dy

            self.dx = self.world.pan.angle  # b
            self.x -= self.dx


        elif way == 2:
            self.world.increase_score()
            self.world.count = 1

        elif way == 4:
            self.dy = -1*(self.dy) - 1


class Bowl:
    def __init__(self, world, x, y, angle, radius, color):
        self.world = world
        self.x = x
        self.y = y
        self.angle = angle
        self.radius = radius
        self.color = color

    def update(self, delta):
        pass


class World:
    STATE_FROZEN = 1
    STATE_STARTED = 2

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pan = Pan(self, 50, 200, -15, 400)
        self.bowl = Bowl(self, 650, 450, 0, 30, arcade.color.BLUE_BELL)
        self.state = World.STATE_FROZEN
        self.circle = Circle(self, 350, 700, 0, 0)
        self.score = 0
        self.count = 0

        self.spacebar_hold = False

    def draw_new_bowl(self):
        if self.score >= 20:
            self.bowl.color = arcade.color.RED_DEVIL
            self.bowl.radius = 10
        elif self.score >= 15:
            self.bowl.color = arcade.color.ORANGE
            self.bowl.radius = 15
        elif self.score >= 10:
            self.bowl.color = arcade.color.YELLOW
            self.bowl.radius = 20
        elif self.score >= 5:
            self.bowl.color = arcade.color.WHITE
            self.bowl.radius = 25

    def increase_score(self):
        self.score += 1
        self.circle.y = self.bowl.y
        self.circle.x = self.bowl.x
        self.state = World.STATE_FROZEN

    def get_score(self):
        return self.score

    def reset(self):
        self.circle.x = 350
        self.circle.y = 700
        self.circle.dx = 0
        self.circle.dy = 0
        self.draw_new_bowl()
        self.state = World.STATE_FROZEN

        self.count = 0

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            # Check whether if the circle is in the bowl or not
            if self.count == 1:
                self.reset()
                xpos = randint(600, 900)
                ypos = randint(300, 600)
                self.bowl.x = xpos
                self.bowl.y = ypos
                self.count = 0
            self.spacebar_hold = True

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.spacebar_hold = False

    def update(self, delta):
        if self.state == World.STATE_FROZEN:
            return
        hit_pan = False
        hit_bowl = False
        xc = self.circle.x
        yc = self.circle.y
        yc2 = self.circle.y - self.circle.dy

        for ball in self.pan.ball:
            x = self.pan.x + ball * math.cos(self.pan.angle/55)
            y = self.pan.y + ball * math.sin(self.pan.angle/55)+40
            r = 10
            if r**2 + 10 >= (x-xc)**2 + (y-yc)**2:
                hit_pan = True
            if r**2 + 10 >= (x-xc)**2 + (y-yc2)**2:
                hit_pan = True

        # detect collision แบบทรงกลม
        if self.bowl.x-self.bowl.radius-r <= self.circle.x <= self.bowl.x+self.bowl.radius+r and self.bowl.y-self.bowl.radius-r <= self.circle.y <= self.bowl.y+self.bowl.radius+r:
            hit_bowl = True

        if hit_pan:
            arcade.play_sound(arcade.load_sound(
                "audio" + os.sep + "panhit.wav"))
            self.circle.update(delta, 1)
        elif hit_bowl:
            arcade.play_sound(arcade.load_sound(
                "audio" + os.sep + "bowlhit.wav"))
            self.circle.update(delta, 2)
        else:
            self.circle.update(delta, 0)
        self.pan.update(delta)

    def start(self):
        self.state = World.STATE_STARTED

    def freeze(self):
        self.state = World.STATE_FROZEN

    def is_started(self):
        return self.state == World.STATE_STARTED


def is_hit(player_x, player_y, coin_x, coin_y):
    if coin_y - 20 <= player_y + 20:
        if coin_y + 20 <= player_y - 20:
            return False
        if player_x - 20 <= coin_x + 20 and coin_x - 20 <= player_x + 20:
            return True
    return False
