
import pyglet
from pyglet.window import key

width, height = 1280, 720


class Window(pyglet.window.Window):

    square_size = int(height * .2)

    woah_img = pyglet.resource.image('img/woah.gif')

    def __init__(self):
        super().__init__()
        self.set_size(width=width, height=height)
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

        self.woah_img.blit(0, 0)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.A:
            self.square_size = int(height * .5)


if __name__ == '__main__':
    window = Window()
    pyglet.app.run()
