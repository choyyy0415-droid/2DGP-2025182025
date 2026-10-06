from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
SPRITE_SIZE = 100
MOVE_SPEED = 5
IDLE_ROWS = {'right': 300, 'left': 200}
RUN_ROWS = {'right': 100, 'left': 0}


def handle_events(state, pressed):
    for event in get_events():
        if event.type == SDL_QUIT:
            state['running'] = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                state['running'] = False
            elif event.key in pressed:
                pressed[event.key] = True
        elif event.type == SDL_KEYUP and event.key in pressed:
            pressed[event.key] = False


def update_position(state, pressed):
    dx = int(pressed[SDLK_RIGHT]) - int(pressed[SDLK_LEFT])
    dy = int(pressed[SDLK_UP]) - int(pressed[SDLK_DOWN])

    if dx > 0:
        state['facing'] = 'right'
    elif dx < 0:
        state['facing'] = 'left'

    state['x'] += dx * MOVE_SPEED
    state['y'] += dy * MOVE_SPEED

    half = SPRITE_SIZE // 2
    state['x'] = max(half, min(TUK_WIDTH - half, state['x']))
    state['y'] = max(half, min(TUK_HEIGHT - half, state['y']))
    return dx, dy


def main():
    open_canvas(TUK_WIDTH, TUK_HEIGHT)
    tuk_ground = load_image('TUK_GROUND.png')
    character = load_image('animation_sheet.png')

    state = {
        'running': True,
        'x': TUK_WIDTH // 2,
        'y': TUK_HEIGHT // 2,
        'facing': 'right',
        'frame': 0,
    }
    pressed = {
        SDLK_LEFT: False,
        SDLK_RIGHT: False,
        SDLK_UP: False,
        SDLK_DOWN: False,
    }

    close_canvas()


if __name__ == '__main__':
    main()
