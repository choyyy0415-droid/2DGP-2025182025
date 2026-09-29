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


def update_walk_and_run(player):
    if player.action == "walk":
        move_forward(player, 3)
    elif player.action == "run":
        move_forward(player, 8)


def update_jump(player):
    if player.action != "jump":
        player.y = GROUND_Y
        return
    progress = player.frame / (FRAME_COUNT - 1)
    player.y = GROUND_Y + 230 * 4 * progress * (1 - progress)
    move_forward(player, 5)


def attack_lunge(player):
    if player.action != "attack":
        return 0
    distances = (0, 10, 25, 55, 75, 45, 20, 0)
    return distances[player.frame] * player.direction


def advance_frame(player):
    player.frame += 1
    if player.frame == FRAME_COUNT:
        player.frame = 0
        player.loops += 1


def update_pause(player):
    if player.loops < REPEAT_COUNT:
        return False
    if player.pause_started is None:
        player.pause_started = get_time()
    return True


def main():
    open_canvas(900, 600)
    close_canvas()


if __name__ == "__main__":
    main()
