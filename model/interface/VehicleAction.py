from abc import ABC, abstractmethod

class VehicleAction(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def roll(self):
        pass
    
    @abstractmethod
    def brake(self):
        pass