import threading
from model.enumerate.Color import Color
from model.TrafficLight import TrafficLight
from model.Clock import Clock
from typing import List

class Agent:
    """Represents an agent that controls traffic lights.

    This class manages the operation of traffic lights in both X and Y axes, 
    handling the timing for green and yellow lights.

    Attributes:
        id (str): A unique identifier for the agent.
        x_traffic_lights (List[TrafficLight]): Traffic lights on the X axis.
        y_traffic_lights (List[TrafficLight]): Traffic lights on the Y axis.
        current_traffic_lights (List[TrafficLight]): Currently active traffic lights.
        change_time (bool): A flag to indicate whether to switch the timing.
        clock (Clock): An instance of the Clock class for timing control.
        green_time (int): Time in seconds for the green light (default is 15).
        yellow_time (int): Time in seconds for the yellow light (default is 7).
        count (int): Counter for timing the traffic light changes.
    """
     
    def __init__(
            self, id: str, 
            x_traffic_lights: List[TrafficLight], 
            y_traffic_lights: List[TrafficLight],
            x_arrow: List[TrafficLight],
            y_arrow:  List[TrafficLight]
        ):
        """Initializes a new agent.

        Args:
            id (str): The identifier for the agent.
            x_traffic_lights (List[TrafficLight]): Traffic lights on the X axis.
            y_traffic_lights (List[TrafficLight]): Traffic lights on the Y axis.
        """
        self.id = id
        self.x_traffic_lights = x_traffic_lights
        self.y_traffic_lights = y_traffic_lights
        self.x_arrow=x_arrow
        self.y_arrow=y_arrow

        self.current_traffic_lights = self.x_traffic_lights
        self.current_arrow=self.x_arrow
        self.change_time = False
        self.clock = Clock()
        self.clock.add_agent(self)
        
        self.green_time = 15
        self.yellow_time = 7
        self.count = 2
        self.clock_status = True

    def change_color(self, traffic_light: TrafficLight, color: Color):
        traffic_light.color = color

    def start_clock(self):
        """Starts the timer for the agent.

        This method begins the countdown for the green light duration.
        """
        print(f"Agent {self.id} is starting the clock")
        for traffic_light in self.x_traffic_lights:
            traffic_light._notify_vehicles()

        for traffic_light in self.y_traffic_lights:
            traffic_light._notify_vehicles()
        
        threading.Thread(target=lambda: self.clock._start(self.green_time)).start()

    def _restart_clock(self):
        """Restarts the timer based on change_time property.

        Switches the timing between green and yellow lights.
        """
        if not self.clock_status:
            return
        
        self.change_time = not self.change_time
        print(f"Agent {self.id} is restarting the clock")
        
        self._update_traffic_lights(self.current_traffic_lights,self.current_arrow)
        if self.change_time:
            threading.Thread(target=lambda: self.clock._start(self.yellow_time)).start()

        else:
            threading.Thread(target=lambda: self.clock._start(self.green_time)).start()
            

    
    def _check_clock_time(self):
        """Checks the current time on the clock and updates the traffic lights accordingly.

        This method is called when the timer reaches zero, triggering a change in traffic lights.
        """
        self._update_count_and_current_traffic_lights()
        self._restart_clock()

    def _update_count_and_current_traffic_lights(self):
        """Updates the count for timing and switches the current traffic lights.

        When the count reaches zero, the method changes the active traffic lights 
        from X to Y axis or vice versa.
        """
        self.count -= 1
        print(f"\nI am the agent {self.id} and my count is {self.count}")
        if self.count == 0:
            print("="*100)
            print("CHANGING TRAFFIC LIGHTS")
            print("="*100)
            self.count = 2
            self._update_traffic_lights(self.current_traffic_lights,self.current_arrow)

            if self.current_traffic_lights == self.x_traffic_lights:
                print(f"I am the agent {self.id}, I am going to change current traffic lights to Y-axis")
                self.current_traffic_lights = self.y_traffic_lights
                self.current_arrow = self.y_arrow
            else:
                print(f"I am the agent {self.id}, I am going to change current traffic lights to X-axis")
                self.current_traffic_lights = self.x_traffic_lights
                self.current_arrow = self.x_arrow
            print("")

    def _update_traffic_lights(self, traffic_lights: List[TrafficLight], arrows: List[TrafficLight]):
        """Updates the color of the specified traffic lights.

        Args:
            traffic_lights (List[TrafficLight]): The list of traffic lights to be updated.
        """
        for traffic_light in traffic_lights:
            traffic_light.next_color()


        for arrow in arrows:
            if traffic_light.color== Color.YELLOW or traffic_light.color == Color.GREEN:
                arrow.next_arrow()