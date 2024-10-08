from interface.VehicleAction import VehicleAction
from enumerate.Color import Color

class Vehicle(VehicleAction):
    def __init__(self, license_plate: str):
        self.license_plate = license_plate
        self.traffic_light = None

    def start(self):
        print(f"{self.license_plate} starting.")
    
    def roll(self):
        print(f"{self.license_plate} rolling.")
    
    def brake(self):
        print(f"{self.license_plate} braking.")

    def stop(self):
        print(f"{self.license_plate} stopped.")

    def _check_traffic_light(self):
        match self.traffic_light.color:
            case Color.GREEN:
                self.start()
                self.roll()
            case Color.YELLOW:
                self.brake()
            case Color.RED:
                self.stop()