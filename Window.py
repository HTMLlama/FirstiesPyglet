
import pyglet

from pyglet.window import key
from pyglet.gl import *

width, height = 1280, 720
center = width // 2, height // 2


class Window(pyglet.window.Window):
    background = 94, 0, 123, 255
    background_img = pyglet.image.SolidColorImagePattern(background).create_image(width, height)

    box_size = int(height * .1)
    box_x, box_y = int(width * .2), int(height * .5)

    woah_img = pyglet.resource.image('img/woah.gif')

    woah_gif = pyglet.image.load_animation('img/woah.gif')
    skate_park_gif = pyglet.image.load_animation('img/skate_park.gif')
    space_gif = pyglet.image.load_animation('img/space.gif')
    bin = pyglet.image.atlas.TextureBin()
    sprite = pyglet.sprite.Sprite(space_gif, usage='dynamic')
    img_loc = center[0] + sprite.width, center[1] + sprite.height

    woah_gif.add_to_texture_bin(bin)
    skate_park_gif.add_to_texture_bin(bin)
    space_gif.add_to_texture_bin(bin)

    sprite.x, sprite.y = 600, 250
    sprite.scale = .5
    sprite_speed = 9
    wMod, aMod, sMod, dMod = 0, 0, 0, 0

    def __init__(self):
        super().__init__(width, height, resizable=True, vsync=True)
        self.set_minimum_size(300, 200)
        self.set_maximum_size(1920, 1080)
        self.set_caption('Woah Pyglet')

    def on_draw(self):
        self.clear()
        self.background_img.blit(0, 0)

        box_coorods = (self.box_x, self.box_y,
                       self.box_x, int(self.box_y + self.box_size),
                       int(self.box_x + self.box_size), self.box_y,
                       int(self.box_x + self.box_size), int(self.box_y + self.box_size))

        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, [0, 1, 2, 1, 2, 3], ('v2i', box_coorods))

        self.sprite.update(x=self.sprite.x + self.aMod + self.dMod, y=self.sprite.y + self.wMod + self.sMod)
        self.sprite.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.A: self.aMod = -self.sprite_speed
        elif symbol == key.D: self.dMod = self.sprite_speed
        elif symbol == key.W: self.wMod = self.sprite_speed
        elif symbol == key.S: self.sMod = -self.sprite_speed

    def on_key_release(self, symbol, modifiers):
        if symbol == key.A: self.aMod = 0
        elif symbol == key.D: self.dMod = 0
        elif symbol == key.W: self.wMod = 0
        elif symbol == key.S: self.sMod = 0

    def update(self, dt):
        self.sprite.x += dt * 10

