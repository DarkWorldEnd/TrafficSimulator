from enumerate.Direction import Direction
from TrafficLight import TrafficLight
from typing import Dict

class Intersection:
    def __init__(self):
        self.traffic_lights: Dict[Direction, TrafficLight] = {}
        self.crosswalks: Dict[Direction, bool] = {}

    def add_traffic_light(self, direction, traffic_light):
        self.traffic_lights[direction] = traffic_light

    def add_cross_walk(self, direction, exist):
        self.crosswalks[direction] = exist