from os.path import abspath, dirname, join
from pico2d import *

open_canvas(800, 600)

# character.png 파일을 현재 파이썬 파일이 있는 폴더에서 불러온다.
image_path = join(dirname(abspath(__file__)), 'character.png')
boy = load_image(image_path)

clear_canvas()
boy.draw(400, 300)
update_canvas()
delay(1)


def move_circle():
    pass


def move_rectangle():
    pass


def move_triangle():
    pass


while True:
    move_circle()
    move_rectangle()
    move_triangle()
