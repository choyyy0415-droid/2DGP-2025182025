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


    @staticmethod
    def draw(boy):
        row = 100 if boy.face_dir == 1 else 0
        boy.image.clip_draw(int(boy.frame) * 100, row, 100, 100,
                            boy.x, 115, AutoRun.SIZE, AutoRun.SIZE)


class Boy:
    image = None

    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0.0
        self.face_dir = 1
        self.keys = []
        if Boy.image is None:
            Boy.image = load_image(str(Path(__file__).with_name('animation_sheet.png')))
        self.machine = Machine(
            model=self, states=['IDLE', 'SLEEP', 'RUN',
                                {'name': 'AUTO_RUN', 'on_enter': 'enter_auto'}], initial='IDLE',
            auto_transitions=False,
            after_state_change='enter_state',
            transitions=[
                ['time_out', 'IDLE', 'SLEEP'],
                ['wake_up', 'SLEEP', 'IDLE'],
                ['start_run', ['IDLE', 'SLEEP', 'AUTO_RUN'], 'RUN'],
                ['stop_run', 'RUN', 'IDLE'],
                ['start_auto', 'IDLE', 'AUTO_RUN'],
                ['finish_auto', 'AUTO_RUN', 'IDLE'],
            ],
        )
        self.enter_state()


    def enter_state(self):
        self.frame = 0.0
        self.idle_started = get_time()
        if self.state != 'AUTO_RUN':
            self.x = max(50, min(750, self.x))


    def enter_auto(self):
        self.keys.clear()
        self.x = max(75, min(725, self.x))
        AutoRun.enter(self)


    def handle_event(self, event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_a:
            if self.state == 'IDLE':
                self.start_auto()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            if self.state == 'SLEEP':
                self.wake_up()
        elif event.type in (SDL_KEYDOWN, SDL_KEYUP) and event.key in (SDLK_LEFT, SDLK_RIGHT):
            if event.type == SDL_KEYDOWN:
                if event.key not in self.keys:
                    self.keys.append(event.key)
            elif event.key in self.keys:
                self.keys.remove(event.key)
            # 두 키를 누르면 나중에 누른 방향을 따른다.
            if self.keys:
                self.face_dir = -1 if self.keys[-1] == SDLK_LEFT else 1
                if self.state != 'RUN':
                    self.start_run()
            elif self.state == 'RUN':
                self.stop_run()


    def update(self, dt):
        if self.state == 'IDLE' and get_time() - self.idle_started >= 5.0:
            self.time_out()
        if self.state != 'SLEEP':
            self.frame = (self.frame + 10 * dt) % 8
        if self.state == 'AUTO_RUN':
            AutoRun.update(self, dt)
        elif self.state == 'RUN':
            self.x = max(50, min(750, self.x + self.face_dir * 200 * dt))


    def draw(self):
        if self.state == 'AUTO_RUN':
            AutoRun.draw(self)
        if self.state == 'RUN':
            row = 100 if self.face_dir == 1 else 0
        else:
            row = 300 if self.face_dir == 1 else 200
        if self.state == 'SLEEP':
            self.image.clip_composite_draw(0, row, 100, 100,
                                           -pi / 2 * self.face_dir, '', self.x, 65, 100, 100)
        elif self.state != 'AUTO_RUN':
            self.image.clip_draw(int(self.frame) * 100, row, 100, 100, self.x, self.y)


running = False
world = []
boy = None

def handle_events():
    global running
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)


def reset_world():
    global world, boy
    boy = Boy()
    world = [Grass(), boy]


