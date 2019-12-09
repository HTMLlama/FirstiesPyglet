
import pyglet

from pyglet.gl import *
from MainGuy import *

width, height = 1280, 720
center = width // 2, height // 2

mobs = []


# noinspection PyAbstractClass
class Window(pyglet.window.Window):
    background = 94, 0, 123, 255
    background_img = pyglet.image.SolidColorImagePattern(background).create_image(width, height)
    main_guy = MainGuy(width, height)

    box_size = int(height * .1)
    box_x, box_y = int(width * .2), int(height * .5)

    woah_img = pyglet.resource.image('img/woah.gif')

    woah_gif = pyglet.image.load_animation('img/woah.gif')
    skate_park_gif = pyglet.image.load_animation('img/skate_park.gif')
    bin = pyglet.image.atlas.TextureBin()

    woah_gif.add_to_texture_bin(bin)
    skate_park_gif.add_to_texture_bin(bin)

    box = (box_x, box_y,
           box_x, int(box_y + box_size),
           int(box_x + box_size), box_y,
           int(box_x + box_size), int(box_y + box_size))

    mobs.append(box)

    def __init__(self):
        super().__init__(width, height, resizable=True, vsync=True)
        self.set_minimum_size(300, 200)
        self.set_maximum_size(1920, 1080)
        self.set_caption('Woah Pyglet')

    def on_draw(self):
        self.clear()
        self.background_img.blit(0, 0)

        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, [0, 1, 2, 1, 2, 3], ('v2i', self.box))

        self.main_guy.update()
        self.main_guy.sprite.draw()
        is_hit = self.check_collision()

    def on_key_press(self, symbol, modifiers):
        self.main_guy.key_down(symbol)

    def on_key_release(self, symbol, modifiers):
        self.main_guy.key_up(symbol)

    def update(self, dt):
        self.main_guy.sprite.x += dt * 10

