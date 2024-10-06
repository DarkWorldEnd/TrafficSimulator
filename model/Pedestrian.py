from interface.PedestrianAction import PedestrianAction

class Pedestrian(PedestrianAction):
    def __init__(self, name: str):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking.")

    def wait(self):
        print(f"{self.name} is waiting.")