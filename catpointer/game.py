import copy
import random
from os import path

import pyxel

from .models import Cat, Point

base_path = path.dirname(__file__)


class App:

    max_jump = 12  # Needs to be even
    max_wait = 20

    def __init__(self):
        pyxel.init(150, 90, caption='Cat Pointer Game')
        pyxel.image(0).load(
            0, 0,
            path.join(base_path, 'assets/cat_16x16.png')
        )
        self.ceiling = 35
        self.floor = 75
        self.cat = Cat(
            x=(pyxel.width // 2) - (Cat.width // 2),
            y=self.floor - Cat.width,
            drawing_area=(0, 0, pyxel.width, self.floor)
        )

        self.point = Point(
            x=pyxel.width//2,
            y=self.ceiling
        )
        self.new_point = copy.copy(self.point)
        self.score = 0
        self.jump = 0
        self.wait = 50

        pyxel.run(self.update, self.draw)

    def pressed(*keys):
        return any(pyxel.btn(key) for key in keys)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.update_cat()
        self.update_point()

        """
        cat_x = self.cat['pos'][0]
        cat_y = self.cat['pos'][1]
        if self.point == self.point_new:
            if cat_x + 1 < self.point[0] < cat_x + 15 and cat_y + 1 < self.point[1] < cat_y + 15:
                self.score += 1
                self.last_frame = pyxel.frame_count - self.wait_time - 1
        """

    def update_cat(self):
        if self.pressed(pyxel.KEY_LEFT, pyxel.KEY_A):
            self.cat.move_left()
        if self.pressed(pyxel.KEY_RIGHT, pyxel.KEY_D):
            self.cat.move_right()

        if self.pressed(pyxel.KEY_SPACE) and not self.cat.is_up:
            self.jump = self.max_jump
        if self.jump > 0:
            self.cat.move_up(1)
            self.jump -= 1
        elif self.cat.is_up:
            self.cat.move_down(2)

    def update_point(self):
        if self.point == self.new_point:
            if self.wait < 0:
                self.new_point = Point(
                    x=random.randint(5, pyxel.width - 5),
                    y=random.randint(self.ceiling + 5, self.floor - 5)
                )
                self.wait = random.randint(10, self.max_wait)
            else:
                self.wait -= 1
        else:
            if self.point.x > self.new_point.x:
                self.point.x -= 1
            if self.point.x < self.new_point.x:
                self.point.x += 1
            if self.point.y > self.new_point.y:
                self.point.y -= 1
            if self.point.y < self.new_point.y:
                self.point.y += 1

    def draw(self):
        pyxel.cls(7)
        self.draw_title()
        self.draw_cat()
        self.draw_point()
        self.draw_score()

    def draw_title(self):
        title = 'Cat Pointer'
        center_x = (pyxel.width // 2) - len(title) * 2
        pyxel.text(center_x, 5, title, 12)

    def draw_cat(self):
        pyxel.blt(
            x=self.cat.x,
            y=self.cat.y,
            img=0,
            sx=self.cat.image_position[0],
            sy=self.cat.image_position[1],
            w=-self.cat.width if self.cat.rigth else self.cat.width,
            h=self.cat.height,
            colkey=self.cat.colkey
        )

    def draw_point(self):
        color = 8
        freq = 15
        frame = pyxel.frame_count % freq
        radius = (
            int(frame < freq/2) 
            if self.point == self.new_point else 0
        )
        pyxel.circ(
            self.point.x, self.point.y, radius, color
        )

    def draw_score(self):
        pyxel.text(10, self.floor + 5, f'Score: {self.score}', 0)


if __name__ == "__main__":
    App()
