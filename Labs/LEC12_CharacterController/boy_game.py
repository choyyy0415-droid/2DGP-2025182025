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


