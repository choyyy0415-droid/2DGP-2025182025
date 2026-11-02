from pathlib import Path

from pico2d import get_canvas_width, get_time, load_image
import game_world


class Ball:
    image = None
    SPEED = 500.0  # pixels per second
    RADIUS = 10.5

    def __init__(self, x, y, direction):
        if Ball.image is None:
            Ball.image = load_image(str(Path(__file__).with_name('ball21x21.png')))
        self.x, self.y = x, y
        self.direction = direction
        self.last_updated = get_time()

    def update(self):
        now = get_time()
        self.x += self.direction * self.SPEED * (now - self.last_updated)
        self.last_updated = now
        if self.x < -self.RADIUS or self.x > get_canvas_width() + self.RADIUS:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
