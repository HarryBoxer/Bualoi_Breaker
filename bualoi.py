import arcade
from random import randint
from pyglet.window import key

SCREEN_WIDTH = 980
SCREEN_HEIGHT = 720

vxs = []
vys = []
xs = []
ys = []
n = 1


class Circle:
    def __init__(self, x, y, vx, vy, r=20):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.r = r

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.x >= SCREEN_WIDTH - self.r:
            self.vx -= 1
        elif self.y >= SCREEN_HEIGHT - self.r:
            self.vy -= 1
        elif self.x <= self.r:
            self.vx += 1
        elif self.y <= self.r:
            self.vy += 1

    def draw(self):
        arcade.draw_circle_outline(self.x, self.y, 20, arcade.color.WHITE)


circle = Circle(700, 100, 0, 10, 20)
keys = key.KeyStateHandler()


def move_circle(i):
    xs += vxs
    ys += vys


def draw_circle(i):
    arcade.draw_circle_outline(xs, ys, 1, arcade.color.BLACK)


def on_draw(delta_time):
    arcade.start_render()

    circle.move()
    circle.draw()


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Circles")
    arcade.set_background_color(arcade.color.GRAY)
    arcade.get_window().push_handlers(keys)
    arcade.schedule(on_draw, 1 / 80)
    arcade.run()


if __name__ == '__main__':
    main()
