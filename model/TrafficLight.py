from enumerate.Color import Color

class TrafficLight:
    def __init__(self, id: str, color: Color):
        self.id = id
        self.color = color
        self.vehicles_observers = []

    def add_vehicle_observer(self, vehicle):
        self.vehicles_observers.append(vehicle)
        vehicle.traffic_light = self

    def next_color(self):
        """Changes the color of the traffic light to the next state.

        The traffic light transitions through the colors: GREEN -> YELLOW -> RED -> GREEN.
        And notifies all vehicles that are observing the traffic light.
        """
        match self.color:
            case Color.GREEN: 
                self.color = Color.YELLOW
                print(f"I am the traffic light {self.id}, Previous color: {Color.GREEN}, Current color: {self.color}")
            case Color.YELLOW: 
                self.color = Color.RED
                print(f"I am the traffic light {self.id}, Previous color: {Color.YELLOW}, Current color: {self.color}")
            case Color.RED: 
                self.color = Color.GREEN
                print(f"I am the traffic light {self.id}, Previous color: {Color.RED}, Current color: {self.color}")
        self._notify_vehicles()

    def _notify_vehicles(self):
        """Notifies all vehicles that are observing the traffic light.

        This method is called when the traffic light changes color.
        """
        for vehicle in self.vehicles_observers:
            vehicle._check_traffic_light()