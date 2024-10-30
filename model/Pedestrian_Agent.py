import threading
from model.enumerate.Color import Color
from model.Pedestrian_Light import Pedestrian_Light
from model.Clock import Clock
from typing import List

class Pedestrian_Agent:
    def __init__(self, id: str, x_pedestrian_lights: List[Pedestrian_Light], y_pedestrian_lights: List[Pedestrian_Light]):
        self.id = id
        self.x_pedestrian_lights = x_pedestrian_lights
        self.y_pedestrian_lights = y_pedestrian_lights
        self.current_pedestrian_light = x_pedestrian_lights  
        self.change_time = False
        self.clock = Clock()
        self.clock.add_agent(self)
        

        self.green_time = 10  
        self.red_time = 12   
        self.clock_status = True

    def start_clock(self):
        print(f"Agent {self.id} is starting the clock")
        threading.Thread(target=lambda: self.clock._start(self.green_time)).start()

    def _restart_clock(self):
        if not self.clock_status:
            return


        self.change_time = not self.change_time
        print(f"Agent {self.id} is restarting the clock")


        if self.change_time:
            self._update_traffic_lights(self.current_pedestrian_light, to_red=True)
            threading.Thread(target=lambda: self.clock._start(self.red_time)).start()
        else:

            self.current_pedestrian_light = self.y_pedestrian_lights if self.current_pedestrian_light == self.x_pedestrian_lights else self.x_pedestrian_lights
            self._update_traffic_lights(self.current_pedestrian_light, to_red=False)
            threading.Thread(target=lambda: self.clock._start(self.green_time)).start()

    def _check_clock_time(self):
        """Checks the current time on the clock and updates the traffic lights accordingly."""
        self._restart_clock()

    def _update_traffic_lights(self, traffic_lights: List[Pedestrian_Light], to_red: bool):
        """Cambia el color de los semáforos a verde o rojo."""
        for traffic_light in traffic_lights:
            if to_red and traffic_light.color == Color.GREEN:
                traffic_light.nextColor()
            elif not to_red and traffic_light.color == Color.RED:
                traffic_light.nextColor()
            print(f"Pedestrian light {traffic_light.id} changed to {traffic_light.color.name}")
