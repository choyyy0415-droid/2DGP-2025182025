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


def main():
    open_canvas(900, 600)
    close_canvas()


if __name__ == "__main__":
    main()
