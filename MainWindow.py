from pyglet.gl import *


class MainWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_maximum_size(600, 480)

    def on_draw(self):
        self.clear()
