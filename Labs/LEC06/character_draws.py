from os.path import abspath, dirname, join
import math
from pico2d import *

open_canvas(800, 600)

# character.png 파일을 현재 파이썬 파일이 있는 폴더에서 불러온다.
image_path = join(dirname(abspath(__file__)), 'character.png')
boy = load_image(image_path)

clear_canvas()
boy.draw(400, 300)
update_canvas()
delay(1)

degree = 0
theta = math.radians(degree)
x = 400 + 200 * math.cos(theta)
y = 300 + 200 * math.sin(theta)


def draw_boy(x, y):
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(0.01)


def move_circle():
    for degree in range(360):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)

        draw_boy(x, y)


def move_rectangle():
    pass


def move_triangle():
    pass


while True:
    move_circle()
    move_rectangle()
    move_triangle()
