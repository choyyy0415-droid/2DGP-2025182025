from os.path import abspath, dirname, join
import math
from pico2d import *

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
CENTER_X = 400
CENTER_Y = 300
CIRCLE_RADIUS = 200
LEFT = 50
RIGHT = 750
BOTTOM = 50
TOP = 550

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

# 어떤 이유에서인지 character.png 파일이 제대로 불러와지지 않아
# 해당 부분은 AI를 통해 수정하였습니다.
image_path = join(dirname(abspath(__file__)), 'character.png')
boy = load_image(image_path)


def draw_boy(x, y):
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(0.01)


degree = 0
theta = math.radians(degree)
x = CENTER_X + CIRCLE_RADIUS * math.cos(theta)
y = CENTER_Y + CIRCLE_RADIUS * math.sin(theta)


def move_circle():
    print('circle')
    for degree in range(360):
        theta = math.radians(degree)
        x = CENTER_X + CIRCLE_RADIUS * math.cos(theta)
        y = CENTER_Y + CIRCLE_RADIUS * math.sin(theta)

        clear_canvas()
        boy.draw(x, y)
        update_canvas()
        delay(0.01)


def move_top():
    print('top')
    for x in range(LEFT, RIGHT + 1, 5):
        draw_boy(x, TOP)
    pass


def move_right():
    print('right')
    for y in range(TOP, BOTTOM - 1, -5):
        draw_boy(RIGHT, y)
    pass


def move_bottom():
    print('bottom')
    for x in range(RIGHT, LEFT - 1, -5):
        draw_boy(x, BOTTOM)
    pass


def move_left():
    print('left')
    for y in range(BOTTOM, TOP + 1, 5):
        draw_boy(LEFT, y)
    pass


def move_rectangle():
    print('rectangle')
    move_top()
    move_right()
    move_bottom()
    move_left()


def move_line(x1, y1, x2, y2):
    for i in range(101):
        t = i / 100
        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t
        draw_boy(x, y)


def move_triangle():
    print('triangle')
    move_line(CENTER_X, TOP, RIGHT, BOTTOM)

    move_line(RIGHT, BOTTOM, LEFT, BOTTOM)

    move_line(LEFT, BOTTOM, CENTER_X, TOP)


while True:
    move_circle()
    move_rectangle()
    move_triangle()
