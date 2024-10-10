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
        self.label = None
        self.direction = None
        self.rolling = False
        self.thread_roll = threading.Thread(target=self.roll)
        self.thread_brake = threading.Thread(target=self.brake)

    def start(self):
        print(f"{self.license_plate} starting.")
    
    def roll(self):
        print(f"{self.license_plate} rolling.")
        self.rolling = True
        # TODO: Falta el debe seguir
        if (self.direction == Direction.EAST):
            print("EAST", self.rolling)
            while self.rolling:
                self.x = self.x + 60 if self.x < 850 else 50
                self.label.move(self.x, 350)
                time.sleep(0.5)

        elif (self.direction == Direction.NORTH):
            print("NORTH", self.rolling)
            while self.rolling:
                self.y = self.y - 60 if self.y > 40 else 700
                self.label.move(500, self.y)           
                time.sleep(0.5)

        print("Thread finished")
    
    def brake(self):
        print
        if self.direction == Direction.EAST:
            if 200 <= self.x <= 700:
                self.rolling = True
                self.thread_roll = threading.Thread(target=self.roll)
                self.thread_roll.start()
            else:
                self.rolling = False

        elif self.direction == Direction.NORTH:
            if 220 <= self.y <= 500:
                self.rolling = True
                self.thread_roll = threading.Thread(target=self.roll)
                self.thread_roll.start()
            else:
                self.rolling = False

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