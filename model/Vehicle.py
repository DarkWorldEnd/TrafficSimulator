from interface.VehicleAction import VehicleAction

class Vehicle(VehicleAction):
    def __init__(self, license_plate: str):
        self.license_plate = license_plate

    def start(self):
        print(f"{self.license_plate} starting.")
    
    def roll(self):
        print(f"{self.license_plate} rolling.")
    
    def brake(self):
        print(f"{self.license_plate} braking.")