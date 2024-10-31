import threading
import time
import random

from model.enumerate.Direction import Direction
from model.enumerate.Color import Color

class Vehicle():
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
        self.active = True
        self.thread_roll = threading.Thread(target=self.roll)
    
    def roll(self):
        haGirado = False
        while self.active:
            while self.direction == Direction.EAST:
                while self.traffic_light and self.traffic_light.color == Color.GREEN:
                    if self.x < 850:
                        self.x = self.x + self.delta
                        
                        if not haGirado and 520<= self.x <= 535:
                            if random.randint(0, 1) == 1:
                                haGirado = True
                                self.direction = Direction.NORTH
                                break
                    
                    else:
                        if haGirado == True:
                            haGirado = False
                            self.direction = Direction.NORTH
                            self.x = 500
                            self.y = 600
                            self.label.move(self.x, self.y)
                            break
                        else: 
                            self.x = 50
                    self.label.move(self.x, self.y)
                    time.sleep(0.1)

                while self.traffic_light and self.traffic_light.color == Color.YELLOW and (self.x > 290 or (0 <= self.x <= 290 - (self.delta + self.label.geometry().width()))):
                    if self.x < 850:
                        self.x = self.x + self.delta
                    else:
                        if haGirado == True:
                            haGirado = False
                            self.direction = Direction.NORTH
                            self.x = 500
                            self.y = 600
                            self.label.move(self.x, self.y)
                            break
                        else: 
                            self.x = 50
                    self.label.move(self.x, self.y)
                    time.sleep(0.1)
            

            while self.direction == Direction.NORTH:
                while self.traffic_light and self.traffic_light.color == Color.GREEN:
                    if self.y > 40:
                        self.y = self.y - self.delta
                        
                        if not haGirado and 365 <= self.y <= 380:
                            # self.direction = Direction.EAST
                            # break
                            if random.randint(0, 1) == 1:
                                haGirado = True
                                self.direction = Direction.EAST
                                break

                    else:
                        if haGirado == True:
                            haGirado = False
                            self.direction = Direction.EAST
                            self.y = 350
                            self.x = 100
                            self.label.move(self.x, self.y)
                            break
                        else:                               
                            self.y = 700
                    # self.y = self.y - self.delta if self.y > 40 else 700
                    self.label.move(self.x, self.y)           
                    time.sleep(0.1)

                while self.traffic_light and self.traffic_light.color == Color.YELLOW and (self.y > 540  or (0 <= self.y <= 540 - self.delta)):
                    if self.y > 40:
                        self.y = self.y - self.delta
                    else:
                        if haGirado == True:
                            haGirado = False
                            self.direction = Direction.EAST
                            self.y = 350
                            self.x = 100
                            self.label.move(self.x, self.y)
                            break
                        else:
                            self.y = 700
                    self.label.move(self.x, self.y)           
                    time.sleep(0.1)


    def _check_traffic_light(self):
        match self.traffic_light.color:
            case Color.GREEN:
                pass

            case Color.YELLOW:
                pass

            case Color.RED:
                pass