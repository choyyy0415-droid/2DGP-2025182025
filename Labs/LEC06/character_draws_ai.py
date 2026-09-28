from os.path import abspath, dirname, join
import math
from pico2d import *

open_canvas(800, 600)

image_path = join(dirname(abspath(__file__)), 'character.png')
boy = load_image(image_path)
running = True


def handle_events():
    global running
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def draw_boy(x, y):
    handle_events()
    if not running:
        return
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(0.01)


def move_circle():
    for degree in range(360):
        if not running:
            return
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)
        draw_boy(x, y)


def move_top():
    for x in range(50, 751, 5):
        if not running:
            return
        draw_boy(x, 550)


def move_right():
    for y in range(550, 49, -5):
        if not running:
            return
        draw_boy(750, y)


def move_bottom():
    for x in range(750, 49, -5):
        if not running:
            return
        draw_boy(x, 50)


def move_left():
    for y in range(50, 551, 5):
        if not running:
            return
        draw_boy(50, y)


def move_rectangle():
    move_top()
    move_right()
    move_bottom()
    move_left()


def move_line(x1, y1, x2, y2):
    for i in range(101):
        if not running:
            return
        t = i / 100
        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t
        draw_boy(x, y)


def move_triangle():
    move_line(400, 550, 750, 50)
    move_line(750, 50, 50, 50)
    move_line(50, 50, 400, 550)


while running:
    move_circle()
    move_rectangle()
    move_triangle()

close_canvas()
