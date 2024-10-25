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
        self.current_pedestrian_light = x_pedestrian_lights  # Comienza con las luces peatonales en 'x'
        self.change_time = False
        self.clock = Clock()
        self.clock.add_agent(self)
        self.green_time = 10
        self.red_time = 12
        self.count = 2
        self.clock_status = True

    def change_color(self, pedestrian_light: Pedestrian_Light, color: Color):
        pedestrian_light.color = color
        pedestrian_light.update_image()  # Asegúrate de que este método actualice la imagen en la GUI

    def start_clock(self):
        print(f"Agent {self.id} is starting the clock")
        threading.Thread(target=lambda: self.clock._start(self.green_time)).start()

    def _restart_clock(self):
        if not self.clock_status:
            return

        self.change_time = not self.change_time
        print(f"Agent {self.id} is restarting the clock")

        # Actualiza el color de las luces peatonales
        self._update_traffic_lights(self.current_pedestrian_light)

        # Cambia el tiempo según el estado actual
        if self.change_time:
            threading.Thread(target=lambda: self.clock._start(self.red_time)).start()
        else:
            threading.Thread(target=lambda: self.clock._start(self.green_time)).start()

    def _check_clock_time(self):
        self._update_count_and_current_traffic_lights()
        self._restart_clock()

    def _update_count_and_current_traffic_lights(self):
        self.count -= 1
        print(f"\nAgent {self.id} - Count: {self.count}")
        if self.count == 0:
            print("=" * 50)
            print("CHANGING PEDESTRIAN TRAFFIC LIGHTS")
            print("=" * 50)
            self.count = 2  # Reinicia el contador

            # Actualiza el color de las luces peatonales
            self._update_traffic_lights(self.current_pedestrian_light)

            # Alterna entre los semáforos de 'x' e 'y'
            if self.current_pedestrian_light == self.x_pedestrian_lights:
                self.current_pedestrian_light = self.y_pedestrian_lights
            else:
                self.current_pedestrian_light = self.x_pedestrian_lights

    def _update_traffic_lights(self, traffic_lights: List[Pedestrian_Light]):
        for traffic_light in traffic_lights:
            traffic_light.nextColor()  # Alterna al siguiente color
