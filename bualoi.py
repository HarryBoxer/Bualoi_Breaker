import arcade
import math
from random import randint
from models import World
from pyglet.window import key

SCEEN_TITLE = "Bualoi"

SCREEN_WIDTH = 980
SCREEN_HEIGHT = 720

CIRCLE_RADIUS = 20


class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
            self.angle = self.model.angle

    def draw(self):
        self.sync_with_model()
        super().draw()


class BualoiWindow(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)

        arcade.set_background_color(arcade.color.WHITE_SMOKE)

        self.pan = ModelSprite('images/handpan3.png', model=self.world.pan)
        self.circle = ModelSprite('images/cir.png', model=self.world.circle)

    def on_draw(self):
        arcade.start_render()
        self.pan.draw()

        radius = self.world.bowl.radius
        color = self.world.bowl.color
        arcade.draw_circle_filled(
            self.world.bowl.x, self.world.bowl.y, radius, color)
        self.circle.draw()
        self.draw_score()

    def draw_score(self):
        arcade.draw_text('Score : '+str(self.world.score),
                         self.width - 150,
                         self.height - 30,
                         arcade.color.BLACK,
                         20, )

    def on_key_press(self, key, key_modifiers):
        if not self.world.is_started():
            self.world.start()
        if key == arcade.key.SPACE:
            if self.world.count == 1:
                self.world.on_key_press(key, key_modifiers)
            self.world.on_key_press(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key, key_modifiers)

    def update(self, delta):
        self.world.update(delta)


def main():
    window = BualoiWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()


if __name__ == '__main__':
    main()
