from model.enumerate.Color import Color
from PyQt5 import QtGui

class TrafficLight:
    def __init__(self, id: str, color: Color):
        self.id = id
        self.color = color
        self.vehicles_observers = []
        self.label = None

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
                self.label.setPixmap(QtGui.QPixmap("./img/a.jpg"))

            case Color.YELLOW: 
                self.color = Color.RED
                self.label.setPixmap(QtGui.QPixmap("./img/r.jpg"))

            case Color.RED: 
                self.color = Color.GREEN
                self.label.setPixmap(QtGui.QPixmap("./img/v.jpg"))
                
        self._notify_vehicles()

    def next_arrow(self):
        match self.color:
            case Color.GREEN: 
                self.color = Color.RED
                self.label.setPixmap(QtGui.QPixmap("./img/fr.jpg"))

            case Color.RED: 
                self.color = Color.GREEN
                self.label.setPixmap(QtGui.QPixmap("./img/fv.jpg"))
        self._notify_vehicles()

    def _notify_vehicles(self):
        """Notifies all vehicles that are observing the traffic light.

        This method is called when the traffic light changes color.
        """
        for vehicle in self.vehicles_observers:
            vehicle._check_traffic_light()