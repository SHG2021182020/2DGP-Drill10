from pico2d import *
import game_world
import game_framework

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Bird:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.action, self.frame = 0, 0

    def draw(self):
        if self.velocity > 0:
            self.image.clip_composite_draw(int(self.frame) % 5 * 918 // 5, self.action * 506 // 3, 918 // 5 - 5, 506 // 3,
                                           0, '', self.x, self.y, 918 // 10, 506 // 6)
        if self.velocity < 0:
            self.image.clip_composite_draw(int(self.frame) % 5 * 918 // 5, self.action * 506 // 3, 918 // 5 - 5, 506 // 3,
                                           0, 'h', self.x, self.y, 918 // 10, 506 // 6)

    def update(self):
        self.x += self.velocity * RUN_SPEED_PPS * game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

        if(self.frame < 5):
            self.action = 0
        elif(self.frame < 10):
            self.action = 1
        else:
            self.action = 2

        if self.x < 25 or self.x > 1600 - 918 // 5:
            self.velocity *= -1