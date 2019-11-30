
import pyglet
from pyglet.window import key
from pyglet.image import Texture
from pyglet.gl import *

width, height = 1280, 720
center = width // 2, height // 2


class Window(pyglet.window.Window):

    square_size = int(height * .2)

    woah_img = pyglet.resource.image('img/woah.gif')

    woah_gif = pyglet.image.load_animation('img/woah.gif')
    bin = pyglet.image.atlas.TextureBin()
    sprite = pyglet.sprite.Sprite(woah_gif, usage='dynamic')
    img_loc = center[0] + sprite.width, center[1] + sprite.height

    woah_gif.add_to_texture_bin(bin)
    sprite.x, sprite.y = 250, 250
    xMod, yMod = 0, 0

    def __init__(self):
        super().__init__(width, height, resizable=True)
        self.set_size(width=self.width, height=self.height)
        self.set_minimum_size(300, 200)
        self.set_maximum_size(1920, 1080)
        self.set_caption('Woah Pyglet')

    def on_draw(self):
        self.clear()
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                     [0, 1, 2, 1, 2, 3],
                                     ('v2i', (int(width * .2), int(height * .5),
                                              int(width * .2), int(height * .5 + self.square_size),
                                              int(width * .2 + self.square_size), int(height * .5),
                                              int(width * .2 + self.square_size), int(height * .5 + self.square_size))))

        # self.woah_img.blit(0, 0)
        self.sprite.update(x=self.sprite.x + self.xMod, y=self.sprite.y + self.yMod)
        self.sprite.draw()

    def on_resize(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(gl.GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, width, 0, height, -1, 1)
        glMatrixMode(gl.GL_MODELVIEW)
        return pyglet.event.EVENT_HANDLED

    def on_key_press(self, symbol, modifiers):
        # if symbol == key.A: self.sprite.update(x=self.sprite.x - 10)
        # elif symbol == key.D: self.sprite.update(x=self.sprite.x + 10)
        # elif symbol == key.W: self.sprite.update(y=self.sprite.y + 10)
        # elif symbol == key.S: self.sprite.update(y=self.sprite.y - 10)

        if symbol == key.A: self.xMod = -12
        elif symbol == key.D: self.xMod = 12
        elif symbol == key.W: self.yMod = 12
        elif symbol == key.S: self.yMod = -12

    def on_key_release(self, symbol, modifiers):
        if symbol == key.A: self.xMod = 0
        elif symbol == key.D: self.xMod = 0
        elif symbol == key.W: self.yMod = 0
        elif symbol == key.S: self.yMod = 0

    def update(self, dt):
        self.sprite.x += dt * 10


if __name__ == '__main__':
    window = Window()
    pyglet.clock.schedule_interval(window.update, 1 // 60)
    pyglet.app.run()
