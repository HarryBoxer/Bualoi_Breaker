import arcade
from random import randint
from models import World
from pyglet.window import key

SCREEN_WIDTH = 980
SCREEN_HEIGHT = 720

vxs = []
vys = []
xs = []
ys = []
n = 1

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)

    def draw(self):
        self.sync_with_model()
        super().draw()

# circle = Circle(700, 100, 0, 10, 20)
# keys = key.KeyStateHandler()


# def move_circle(i):
#     xs += vxs
#     ys += vys

class BualoiWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE_SMOKE)

        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.pan = ModelSprite('images/handpan2.png', model = self.world.pan)

    def on_draw(self):
        arcade.start_render()
        self.pan.draw()

    def update(self, delta):
        self.world.update(delta)


# def draw_circle(i):
#     arcade.draw_circle_outline(xs, ys, 1, arcade.color.BLACK)


    # circle.move()
    # circle.draw()


def main():
    window = BualoiWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    # arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Circles")
    # arcade.set_background_color(arcade.color.GRAY)
    # arcade.get_window().push_handlers(keys)
    # arcade.schedule(on_draw, 1 / 80)
    arcade.run()


if __name__ == '__main__':
    main()
