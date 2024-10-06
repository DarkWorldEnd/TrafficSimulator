from TrafficLight import TrafficLight
from enumerate.Color import Color
from typing import List

class Agent:
    def __init__(self, id: str, traffic_lights: List[TrafficLight]):
        self.id = id
        self.traffic_lights = traffic_lights

    def change_color(self, traffic_light: TrafficLight, color: Color):
        traffic_light.color = color