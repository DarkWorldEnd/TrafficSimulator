from abc import ABC, abstractmethod

class PedestrianAction(ABC):
    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def wait(self):
        pass