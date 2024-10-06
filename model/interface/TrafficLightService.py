from abc import ABC, abstractmethod

class TrafficLightService(ABC):
    @abstractmethod
    def subscribe(self, vehicle):
        pass

    @abstractmethod
    def unsubscribe(self, vehicle):
        pass

    @abstractmethod
    def notifyColor(self):
        pass