from pico2d import *
import random

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
BALL_COUNT = 11

class Boy:
    def __init__(self):
        # 소년별로 시작 위치를 다르게 한다.
        self.x, self.y = random.randint(100, 700), 90

        # 애니메이션 시작 프레임을 다르게 한다.
        self.frame = random.randint(0, 7)

        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(
            self.frame * 100,
            0,
            100,
            100,
            self.x,
            self.y
        )
class Ball:
    def __init__(self):
        # 공마다 위치와 속도를 다르게 설정한다.
        self.x = random.randint(20, CANVAS_WIDTH - 20)
        self.y = random.randint(CANVAS_HEIGHT, CANVAS_HEIGHT + 500)
        self.speed = random.randint(3, 10)

        self.image = load_image('ball21x21.png')

    def update(self):
        # 공을 아래쪽으로 이동시킨다.
        self.y -= self.speed

        # 화면 아래로 나가면 다시 위에서 떨어지게 한다.
        if self.y < -20:
            self.x = random.randint(20, CANVAS_WIDTH - 20)
            self.y = random.randint(
                CANVAS_HEIGHT,
                CANVAS_HEIGHT + 300
            )
            self.speed = random.randint(3, 10)

    def draw(self):
        self.image.draw(self.x, self.y, 42, 42)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)



class Zombie:
    def __init__(self):
        self.x, self.y = 100, 170
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 5

    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h

        self.image.clip_draw(
            self.frame * frame_width,
            0,
            frame_width,
            frame_height,
            self.x,
            self.y,
            frame_width // 2,
            frame_height // 2
        )


def handle_events():
    global running

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False


def reset_world():
    global running
    global world

    running = True
    world = []
    ball = Ball()
    world.append(ball)
    # 잔디 객체를 생성하여 월드에 넣는다.
    grass = Grass()
    world.append(grass)

    # 소년 객체 11명을 생성하여 월드에 넣는다.
    world= [Boy() for i in range(11)]
   
     # 공 객체 11개를 생성한다.
    world = [Ball() for i in range(BALL_COUNT)]
  
    # 좀비 객체를 생성하여 월드에 넣는다.
    zombie = Zombie()
    world.append(zombie)


def update_world():
    for o in world:
        o.update()


def render_world():
    clear_canvas()

    for o in world:
        o.draw()

    update_canvas()


open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.02)

close_canvas()

