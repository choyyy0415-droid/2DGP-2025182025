from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
SPRITE_SIZE = 100
MOVE_SPEED = 5
IDLE_ROWS = {'right': 300, 'left': 200}
RUN_ROWS = {'right': 100, 'left': 0}


def main():
    open_canvas(TUK_WIDTH, TUK_HEIGHT)
    tuk_ground = load_image('TUK_GROUND.png')
    character = load_image('animation_sheet.png')

    close_canvas()


if __name__ == '__main__':
    main()
