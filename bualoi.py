import arcade
import math
from random import randint
from models import World
from pyglet.window import key

SCREEN_WIDTH = 980
SCREEN_HEIGHT = 720

CIRCLE_RADIUS = 20


# vxs = []
# vys = []
# xs = []
# ys = []
# n = 1


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

# circle = Circle(700, 100, 0, 10, 20)
# keys = key.KeyStateHandler()


# def move_circle(i):
#     xs += vxs
#     ys += vys

# p
# class ball:
#     def __init__(self, pan):
#         self.ball = pan.ball
#         self.angle = pan.angle
#         self.x = pan.x
#         self.y = pan.y

#     def on_draw(self,angle):
#         for ball in self.ball:
#             arcade.draw_circle_filled(
#                 self.x + (ball * math.cos(angle/55)), self.y + (ball * math.sin(angle/55))+20 , 10, arcade.color.YELLOW_ORANGE)


class BualoiWindow(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)

        arcade.set_background_color(arcade.color.WHITE_SMOKE)
        # self.background = arcade.load_texture('images/background.png')

        self.pan = ModelSprite('images/handpan3.png', model=self.world.pan)
        self.circle = ModelSprite('images/cir.png', model=self.world.circle)

        # self.bowl = ModelSprite('images/bowl.png', model=self.world.bowl)
        # self.bowl = arcade.draw_circle_filled(self.world.circle.x, self.world.circle.y, 20, arcade.color.BLACK)

        # self.ball = ball(self.world.pan)

    def on_draw(self):
        # temp_radius = self.world.bowl.radius
        arcade.start_render()
        # arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
        #                                SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.pan.draw()

        # if self.world.score >= 1:
        #     temp_radius == 5 
        radius = self.world.bowl.radius
        color = self.world.bowl.color
        arcade.draw_circle_filled(self.world.bowl.x, self.world.bowl.y,radius , color)
        self.circle.draw()
        # self.bowl.draw()
        self.draw_score()
        # p
        # self.ball.on_draw(self.world.pan.angle)

    def draw_score(self):
        arcade.draw_text('Score : '+str(self.world.score),
                         self.width - 150,
                         self.height - 30,
                         arcade.color.BLACK,
                         20, )

    def on_key_press(self, key, key_modifiers):
        if not self.world.is_started():
            self.world.start()
            # self.world.reset()
        if key == arcade.key.SPACE:
            if self.world.count == 1:
                self.world.on_key_press(key, key_modifiers)
            self.world.on_key_press(key, key_modifiers)

    # def on_key_press(self, key, key_modifiers):
    #     self.world.on_key_press(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key, key_modifiers)

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
