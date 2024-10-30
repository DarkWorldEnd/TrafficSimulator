import threading
import time

from model.interface.VehicleAction import VehicleAction
from model.enumerate.Direction import Direction
from model.enumerate.Color import Color

class Vehicle(VehicleAction):
    def __init__(self, license_plate: str):
        self.license_plate = license_plate
        self.traffic_light = None
        self.traffic_arrow = None
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
        while (self.direction == Direction.EAST):
            while self.traffic_light and self.traffic_light.color == Color.GREEN:
                self.x = self.x + self.delta if self.x < 850 else 50
                self.label.move(self.x, 350)
                time.sleep(0.1)

            while self.traffic_light and self.traffic_light.color == Color.YELLOW and self.x > 290 or (0 <= self.x <= 290 - (self.delta + self.label.geometry().width())):
                self.x = self.x + self.delta if self.x < 850 else 50
                self.label.move(self.x, 350)
                time.sleep(0.1)
            

        while (self.direction == Direction.NORTH):
            while self.traffic_light and self.traffic_light.color == Color.GREEN:
                self.y = self.y - self.delta if self.y > 40 else 700
                self.label.move(500, self.y)           
                time.sleep(0.1)

            while self.traffic_light and self.traffic_light.color == Color.YELLOW and (self.y > 540  or (0 <= self.y <= 540 - self.delta)):
                self.y = self.y - self.delta if self.y > 40 else 700
                self.label.move(500, self.y)           
                time.sleep(0.1)

    def brake(self):
        if self.direction == Direction.EAST:
           
            # Keep rolling after zebra crossing and before arrive to it
            while self.x > 290 or (0 <= self.x <= 290 - (self.delta + self.label.geometry().width())):
                self.x = self.x + self.delta if self.x < 850 else 50
                self.label.move(self.x, 350)
                time.sleep(0.1)

        elif self.direction == Direction.NORTH:
            # if 220 <= self.y <= 500:
            #     self.rolling = True
            #     self.thread_roll = threading.Thread(target=self.roll)
            #     self.thread_roll.start()
            pass

    def stop(self):
        if self.direction == Direction.EAST:
            pass
        else:
            self.rolling = False
        print(f"{self.license_plate} stopped.")

    def _check_traffic_light(self):
        print("Checking traffic light")
        match self.traffic_light.color:
            case Color.GREEN:
                pass

            case Color.YELLOW:
                pass

            case Color.RED:
                
                pass