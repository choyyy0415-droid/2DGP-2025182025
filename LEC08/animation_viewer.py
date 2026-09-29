from pathlib import Path

from pico2d import *

WIDTH, HEIGHT = 900, 600
FPS = 12
GROUND_Y = 285
ROOT = Path(__file__).parents[1]
CHARACTER_PATH = ROOT / "LEC05" / "character.png"
BACKGROUND_PATH = ROOT / "LEC05" / "grass.png"
ACTIONS = ("walk", "run", "jump", "attack")
FRAME_COUNT = 8
REPEAT_COUNT = 5
PAUSE_SECONDS = 1.0


class Player:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = GROUND_Y
        self.direction = 1
        self.action_index = 0
        self.frame = 0
        self.loops = 0
        self.pause_started = None

    @property
    def action(self):
        return ACTIONS[self.action_index]


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            return False
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            return False
    return True


def move_forward(player, speed):
    player.x += speed * player.direction
    if player.x > WIDTH - 120:
        player.x = WIDTH - 120
        player.direction = -1
    elif player.x < 120:
        player.x = 120
        player.direction = 1


def main():
    open_canvas(900, 600)
    close_canvas()


if __name__ == "__main__":
    main()
