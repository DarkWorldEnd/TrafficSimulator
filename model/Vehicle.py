import threading
import time

from model.interface.VehicleAction import VehicleAction
from model.enumerate.Direction import Direction
from model.enumerate.Color import Color

class Vehicle(VehicleAction):
    def __init__(self, license_plate: str):
        self.license_plate = license_plate
        self.traffic_light = None
        self.x = 0
        self.y = 0
        self.delta = 15
        self.label = None
        self.direction = None
        self.rolling = False
        self.thread_roll = threading.Thread(target=self.roll)

    def start(self):
        print(f"{self.license_plate} starting.")
    
    def roll(self):
        print(f"{self.license_plate} rolling.")
        self.rolling = True
        if (self.direction == Direction.EAST):
            while self.rolling:
                self.x = self.x + self.delta if self.x < 850 else 50
                self.label.move(self.x, 350)
                time.sleep(0.1)

                if self.traffic_light.color == Color.YELLOW and (130 <= self.x <= 290):
                    self.rolling = False
                    

        elif (self.direction == Direction.NORTH):
            while self.rolling:
                self.y = self.y - self.delta if self.y > 40 else 700
                self.label.move(500, self.y)           
                time.sleep(0.1)

                if self.traffic_light.color == Color.YELLOW and (500<= self.y <= 640):
                    self.rolling = False

    
    def brake(self):
        if self.direction == Direction.EAST:
            if 200 <= self.x <= 700:
                self.rolling = True
                self.thread_roll = threading.Thread(target=self.roll)
                self.thread_roll.start()

        elif self.direction == Direction.NORTH:
            if 220 <= self.y <= 500:
                self.rolling = True
                self.thread_roll = threading.Thread(target=self.roll)
                self.thread_roll.start()

    def stop(self):
        self.rolling = False
        print(f"{self.license_plate} stopped.")

    def _check_traffic_light(self):
        print("Checking traffic light")
        match self.traffic_light.color:
            case Color.GREEN:
                self.start()
                self.thread_roll = threading.Thread(target=self.roll)
                self.thread_roll.start()

            case Color.YELLOW:
                self.brake()

            case Color.RED:
                self.stop()