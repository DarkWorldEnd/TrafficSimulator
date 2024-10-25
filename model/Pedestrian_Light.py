from model.enumerate.Color import Color
from PyQt5 import QtGui

class Pedestrian_Light:
    def __init__(self, id: str, color:Color):
        self.id= id
        self.color=color
        self.pedestrian_observers=[]
        self.label = None

    def add_pedestrian_observer(self, pedestrian):
        self.pedestrian_observers.append(pedestrian)
        pedestrian.pedestrian_light= self

    def nextColor(self):
        match self.color:
            case Color.GREEN: 
                self.color = Color.RED
                self.label.setPixmap(QtGui.QPixmap("./img/pr.png"))

            case Color.RED: 
                self.color = Color.GREEN
                self.label.setPixmap(QtGui.QPixmap("./img/pv.png"))
                
        self._notify_pedestrian()
    


    def _notify_pedestrian(self):
        """Notifies all pedestrian that are observing the traffic light.

        This method is called when the traffic light changes color.
        """
        for pedestrian in self.pedestrian_observers:
            #pedestrian._check_pedestrian_light()
            pass
