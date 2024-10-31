import threading
import time

from model.enumerate.Direction import Direction
from model.enumerate.Color import Color

class Pedestrian():
    def __init__(self, name: str):
        self.name = name
        self.x = 0
        self.y = 0
        self.delta = 5
        self.label = None
        self.active = True
        self.direction = None
        self.pedestrian_light = None
        self.thread = threading.Thread(target=self.move)

    def move(self):
        while self.active and self.direction == Direction.EAST:
            while self.pedestrian_light and self.pedestrian_light.color == Color.GREEN:
                self.x = self.x + self.delta if self.x < 610 else 380
                self.label.move(self.x, self.y)
                time.sleep(0.1)

            while self.pedestrian_light and self.pedestrian_light.color == Color.RED and (self.x > 380):
                self.x = self.x + self.delta if self.x < 610 else 380
                self.label.move(self.x, self.y)
                time.sleep(0.1)

        while self.active and self.direction == Direction.SOUTH:
            while self.pedestrian_light and self.pedestrian_light.color == Color.GREEN:
                self.y = self.y + self.delta if self.y < 460 else 200
                self.label.move(self.x, self.y)           
                time.sleep(0.1)

            while self.pedestrian_light and self.pedestrian_light.color == Color.RED and (self.y > 200):
                self.y = self.y + self.delta if self.y < 460 else 200
                self.label.move(self.x, self.y)           
                time.sleep(0.1)

    def _check_pedestrian_light(self):
        match self.traffic_light.color:
            case Color.GREEN:
                self.active = True
                self.thread.start()

            case Color.YELLOW:
                pass

            case Color.RED:
                self.active = False