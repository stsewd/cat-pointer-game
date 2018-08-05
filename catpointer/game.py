import pyxel
import random
from os import path

from .models import Cat, Point

base_path = path.dirname(__file__)


class App:

    max_jump = 12  # Needs to be even
    wait_time = 60

    def __init__(self):
        pyxel.init(150, 90, caption='Cat Pointer Game')
        pyxel.image(0).load(
            0, 0,
            path.join(base_path, 'assets/cat_16x16.png')
        )

        self.ceiling = 20
        self.floor = 75
        self.cat = Cat(
            x=(pyxel.width // 2) - (Cat.width // 2),
            y=self.floor - Cat.width,
            drawing_area=(0, 0, pyxel.width, self.floor)
        )

        self.point = Point(x=80, y=35)
        self.new_point = Point(x=80, y=35)
        self.score = 0

        self.last_frame = pyxel.frame_count
        self.jump = 0
        self.right = 1

        pyxel.run(self.update, self.draw)

    def pressed(*keys):
        return any(pyxel.btn(key) for key in keys)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        #  self.move_point()
        self.update_cat()

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

    def move_point(self):
        diff_frame = pyxel.frame_count - self.last_frame
        if diff_frame > self.wait_time:
            self.point_new = [
                random.randint(5, pyxel.width - 5),
                random.randint(35, 60),
            ]
            self.last_frame = pyxel.frame_count
        if self.point != self.point_new:
            if self.point_new[0] < self.point[0]:
                self.point[0] -= 1
            if self.point_new[0] > self.point[0]:
                self.point[0] += 1
            if self.point_new[1] < self.point[1]:
                self.point[1] -= 1
            if self.point_new[1] > self.point[1]:
                self.point[1] += 1

    def draw(self):
        pyxel.cls(7)
        self.draw_title()
        self.draw_cat()

        """
        # Display pointer
        if self.point == self.point_new:
            pyxel.circ(*self.point, 1, 8)
        else:
            pyxel.pix(*self.point, 8)
        """
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

    def draw_score(self):
        pyxel.text(10, self.floor + 5, f'Score: {self.score}', 0)


if __name__ == "__main__":
    App()
