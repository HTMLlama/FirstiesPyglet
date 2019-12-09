import pyglet
from pyglet.window import key


class MainGuy:
    space_gif = pyglet.image.load_animation('img/space.gif')
    sprite = pyglet.sprite.Sprite(space_gif, usage='dynamic')
    space_gif.add_to_texture_bin(pyglet.image.atlas.TextureBin())

    width, height = 0, 0
    center = width // 2, height // 2
    sprite.x, sprite.y = 600, 250
    sprite.scale = .5
    sprite_speed = 9
    wMod, aMod, sMod, dMod = 0, 0, 0, 0

    img_loc = center[0] + sprite.width, center[1] + sprite.height

    def __init__(self, width, height):
        self.width, self.height = width, height

    def update(self):
        self.sprite.update(x=self.sprite.x + self.aMod + self.dMod,
                           y=self.sprite.y + self.wMod + self.sMod)

    def key_down(self, symbol):
        if symbol == key.A: self.aMod = -self.sprite_speed
        elif symbol == key.D: self.dMod = self.sprite_speed
        elif symbol == key.W: self.wMod = self.sprite_speed
        elif symbol == key.S: self.sMod = -self.sprite_speed

    def key_up(self, symbol):
        if symbol == key.A: self.aMod = 0
        elif symbol == key.D: self.dMod = 0
        elif symbol == key.W: self.wMod = 0
        elif symbol == key.S: self.sMod = 0

    def distances(self, target):
        return (self.sprite.x - target.x) ** 2 + (self.sprite.y - target.y) ** 2

    def check_collision(self, mobs):
        for i in mobs:
            # Square this distance to compensate
            if self.distances(i) < (self.sprite.width / 2 + i.width / 2) ** 2:
                return True
