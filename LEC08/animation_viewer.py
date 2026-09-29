from pathlib import Path

from pico2d import *

WIDTH, HEIGHT = 900, 600
FPS = 12
GROUND_Y = 285
ROOT = Path(__file__).parents[1]
SHEET_PATH = Path(__file__).with_name("SamuraiSheet.png")
BACKGROUND_PATH = Path(__file__).with_name("TUK_GROUND.png")
ACTIONS = ("walk", "run", "jump", "attack")
CELL_SIZE = 128
DRAW_SIZE = 340
ANIMATIONS = {
    "walk": {"row": 8, "frames": 8, "speed": 3},
    "run": {"row": 7, "frames": 8, "speed": 8},
    "jump": {"row": 6, "frames": 12, "speed": 5},
    "attack": {"row": 5, "frames": 6, "speed": 0},
}
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
        move_forward(player, ANIMATIONS["walk"]["speed"])
    elif player.action == "run":
        move_forward(player, ANIMATIONS["run"]["speed"])


def update_jump(player):
    if player.action != "jump":
        player.y = GROUND_Y
        return
    frame_count = ANIMATIONS["jump"]["frames"]
    progress = player.frame / (frame_count - 1)
    player.y = GROUND_Y + 230 * 4 * progress * (1 - progress)
    move_forward(player, ANIMATIONS["jump"]["speed"])


def attack_lunge(player):
    if player.action != "attack":
        return 0
    distances = (0, 15, 40, 75, 35, 0)
    return distances[player.frame] * player.direction


def advance_frame(player):
    player.frame += 1
    if player.frame == ANIMATIONS[player.action]["frames"]:
        player.frame = 0
        player.loops += 1


def update_pause(player):
    if player.loops < REPEAT_COUNT:
        return False
    if player.pause_started is None:
        player.pause_started = get_time()
    return True


def change_action_after_pause(player):
    if get_time() - player.pause_started < PAUSE_SECONDS:
        return
    player.action_index = (player.action_index + 1) % len(ACTIONS)
    player.frame = 0
    player.loops = 0
    player.pause_started = None


def update_player(player):
    if update_pause(player):
        change_action_after_pause(player)
        return
    update_walk_and_run(player)
    update_jump(player)
    advance_frame(player)


def draw_character(player, sprite_sheet):
    flip = "h" if player.direction < 0 else ""
    animation = ANIMATIONS[player.action]
    sprite_sheet.clip_composite_draw(
        player.frame * CELL_SIZE, animation["row"] * CELL_SIZE,
        CELL_SIZE, CELL_SIZE, 0, flip,
        player.x + attack_lunge(player), player.y,
        DRAW_SIZE, DRAW_SIZE,
    )


def draw_scene(player, sprite_sheet, background):
    clear_canvas()
    background.draw(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
    draw_character(player, sprite_sheet)
    update_canvas()


def main():
    open_canvas(WIDTH, HEIGHT)
    try:
        sprite_sheet = load_image(str(SHEET_PATH))
        background = load_image(str(BACKGROUND_PATH))
        player = Player()
        while handle_events():
            update_player(player)
            draw_scene(player, sprite_sheet, background)
            delay(1.0 / FPS)
    finally:
        close_canvas()


if __name__ == "__main__":
    main()
