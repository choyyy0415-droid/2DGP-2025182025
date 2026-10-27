from pathlib import Path
from math import pi
from pico2d import (open_canvas, close_canvas, get_events, get_time,
                    clear_canvas, update_canvas, delay, load_image,
                    SDL_QUIT, SDL_KEYDOWN, SDL_KEYUP, SDLK_ESCAPE,
                    SDLK_LEFT, SDLK_RIGHT, SDLK_SPACE, SDLK_a)
from transitions import Machine


class Grass:
    image = None

    def __init__(self):
        if Grass.image is None:
            Grass.image = load_image(str(Path(__file__).with_name('grass.png')))

    def update(self, dt):
        pass

    def draw(self):
        self.image.draw(400, 30)


class AutoRun:
    DURATION = 5.0
    SPEED = 400
    SIZE = 150

    @staticmethod
    def enter(boy):
        boy.auto_started = get_time()


    @staticmethod
    def update(boy, dt):
        if get_time() - boy.auto_started >= AutoRun.DURATION:
            boy.finish_auto()
            return
        # 남은 이동 거리까지 반사해 프레임 속도와 무관하게 왕복한다.
        left, right = AutoRun.SIZE / 2, 800 - AutoRun.SIZE / 2
        boy.x += boy.face_dir * AutoRun.SPEED * dt
        while boy.x < left or boy.x > right:
            if boy.x > right:
                boy.x = 2 * right - boy.x
                boy.face_dir = -1
            elif boy.x < left:
                boy.x = 2 * left - boy.x
                boy.face_dir = 1


