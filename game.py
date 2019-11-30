#!/usr/bin/env python
from pyglet.gl import *
import MainWindow

class MainWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.set_minimum_size(600, 480)

    def on_draw(self):
        self.clear()


size = width, height = 1280, 720
# window = pyglet.window.Window(width, height, "Woah Test")
center = midX, midY = width // 2, height // 2

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255

woah = pyglet.image.load_animation("img/woah.gif")

# @window.event
# def on_draw():
#     window.clear()
#     testLabel.draw()
#     exitLabel.draw()

if __name__ == '__main__':
    window = MainWindow(width=width, height=height, caption="Woah Dude!!!!!!!", resizable=True)
    testLabel = pyglet.text.Label("Woah Dude!!!",
                                  x=midX,
                                  y=midY,
                                  anchor_x="center",
                                  anchor_y="center",
                                  font_size=42,
                                  font_name="Didot")

    exitLabel = pyglet.text.Label("Close",
                                  x=window.width ** .2,
                                  y=window.width ** .2,
                                  font_size=16)
    pyglet.app.run()
