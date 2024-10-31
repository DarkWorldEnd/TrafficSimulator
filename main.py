import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication
from PyQt5.QtCore import QTimer, Qt

from model.enumerate.Direction import Direction
from model.enumerate.Color import Color
from model.Agent import Agent
from model.Pedestrian_Agent import Pedestrian_Agent
from model.Pedestrian import Pedestrian
from model.Vehicle import Vehicle
from model.TrafficLight import TrafficLight
from model.Pedestrian_Light import Pedestrian_Light
from view.Vista import Ui_VistaPrincipal


class PrincipalController(QtWidgets.QMainWindow, Ui_VistaPrincipal):
    def __init__(self, parent=None):
        super(PrincipalController, self).__init__(parent)

        self.setupUi(self)

        self.btn_Iniciar.clicked.connect(self.begin)
        self.btn_Detener.clicked.connect(self.stop)

        self.tiempo = 0  
        self.ciclo_duracion = 15 + 7 + 22

        pixmap = QtGui.QPixmap("./img/auto.png")
        
       
        self.Alice = self.createImage(Pedestrian("Alice"), "Alice", 330, 200, 40, 60, "./img/Pedestrian.png", 0)
        # self.Barbara = self.createImage(Pedestrian("Barbara"), "Barbara", 380, 200, 40, 60, "./img/Pedestrian.png", 0)
        # self.Carol = self.createImage(Pedestrian("Carol"), "Carol", 660, 200, 40, 60, "./img/Pedestrian.png", 0)
        self.Dixy = self.createImage(Pedestrian("Dixy"), "Dixy", 380, 470, 40, 60, "./img/Pedestrian.png", 0)

        self.Alice.x = 330
        self.Alice.y = 200

        # self.Barbara.x = 380
        # self.Barbara.y = 200

        # self.Carol.x = 660
        # self.Carol.y = 200

        self.Dixy.x = 380
        self.Dixy.y = 470

        self.Alice.direction = Direction.SOUTH
        # self.Barbara.direction = Direction.EAST
        # self.Carol.direction = Direction.SOUTH
        self.Dixy.direction = Direction.EAST

        self.auto1 = Vehicle("CAR-X")
        self.auto1.direction = Direction.EAST
        self.auto1.x = 100
        self.auto1.y = 350
        self.auto1.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.auto1.label.setGeometry(QtCore.QRect(self.auto1.x, self.auto1.y, 60, 60))        
        self.auto1.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.auto1.label.setScaledContents(True)
        self.auto1.label.setObjectName("auto1")
        self.auto1.label.setPixmap(pixmap)
        self.auto1.label.setMask(pixmap.createMaskFromColor(
            QtGui.QColor(255, 255, 255), QtCore.Qt.MaskMode.MaskInColor
        ))
        self.auto1.direction = Direction.EAST

        self.auto2 = Vehicle("CAR-Y")
        self.auto2.direction = Direction.NORTH
        self.auto2.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.auto2.x = 500
        self.auto2.y = 600
        self.auto2.label.setGeometry(QtCore.QRect(self.auto2.x, self.auto2.y, 60, 60))
        self.auto2.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.auto2.label.setScaledContents(True)
        self.auto2.label.setObjectName("CAR-Y")
        self.auto2.label.setPixmap(pixmap)
        self.auto2.label.setMask(pixmap.createMaskFromColor(
            QtGui.QColor(255, 255, 255), QtCore.Qt.MaskMode.MaskInColor
        ))
        self.auto2.label.setPixmap(
            self.rotar_imagen(QtGui.QPixmap("./img/auto.png"), 270)
        )
        
        aux = self.semaforo1
        self.semaforo1 = TrafficLight("TL-x", Color.GREEN)
        self.semaforo1.axis = "X"
        self.semaforo1.label = aux
        

        aux = self.semaforo2
        self.semaforo2 = TrafficLight("TL-Y", Color.RED)
        self.semaforo2.axis = "Y"
        self.semaforo2.label = aux


        aux=self.flecha1
        self.flecha1=TrafficLight("TLA-X", Color.GREEN)
        self.flecha1.label=aux

        aux=self.flecha2
        self.flecha2=TrafficLight("TLA-Y", Color.RED)
        self.flecha2.label=aux

        self.semaforo1.add_vehicle_observer(self.auto1)
        self.semaforo2.add_vehicle_observer(self.auto2)

        self.flecha1.add_vehicle_observer_arrow(self.auto1)
        self.flecha2.add_vehicle_observer_arrow(self.auto2)

        self.peatonal1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.peatonal2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.peatonal3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.peatonal4.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        aux = self.peatonal1
        self.peatonal1 = Pedestrian_Light("PL-X1", Color.GREEN)
        self.peatonal1.label = aux
        

        aux = self.peatonal3
        self.peatonal3 = Pedestrian_Light("PL-X2", Color.GREEN)
        self.peatonal3.label = aux

        aux = self.peatonal4
        self.peatonal4 = Pedestrian_Light("PL-Y1", Color.RED)
        self.peatonal4.label = aux

        aux = self.peatonal2
        self.peatonal2 = Pedestrian_Light("PL-Y2", Color.RED)
        self.peatonal2.label = aux

        self.peatonal4.add_pedestrian_observer(self.Alice)
        # self.peatonal3.add_pedestrian_observer(self.Barbara)
        # self.peatonal2.add_pedestrian_observer(self.Carol)
        self.peatonal1.add_pedestrian_observer(self.Dixy)
        

        self.agent = Agent("Agent 1", [self.semaforo1], [self.semaforo2], [self.flecha1], [self.flecha2])
        self.pd_agent = Pedestrian_Agent("Agent 2", [self.peatonal1, self.peatonal3], [self.peatonal2, self.peatonal4])

    def createImage(self, reference, object_name, x, y, width, height, path, rotation):
        reference.label = QtWidgets.QLabel(parent=self.centralwidget)
        reference.label.setGeometry(QtCore.QRect(x, y, width, height)) #(x, y, width, height)
        reference.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        reference.label.setScaledContents(True)
        reference.label.setObjectName(object_name)
        pixmap = QtGui.QPixmap(path)
        reference.label.setPixmap(pixmap)
        reference.label.setMask(pixmap.createMaskFromColor(
            QtGui.QColor(255, 255, 255), QtCore.Qt.MaskMode.MaskInColor
        ))
        reference.label.setPixmap(
            self.rotar_imagen(QtGui.QPixmap(path), rotation)
        )

        return reference

    def begin(self):
        self.agent.start_clock()
        self.pd_agent.start_clock()

        self.auto1.thread_roll.start()
        self.auto2.thread_roll.start()
        self.Alice.thread.start()
        # self.Barbara.thread.start()
        # self.Carol.thread.start()
        self.Dixy.thread.start()
        QMessageBox.information(self, "Iniciado", "El programa ha iniciado.")


    def _stop_pedestrian(self, pedestrian):
        pedestrian.active = False
        pedestrian.direction = None
        pedestrian.pedestrian_light = None

    def stop(self):
        self.auto1.direction = None
        self.auto1.traffic_light = None
        self.auto1.active = False

        self.auto2.direction = None
        self.auto2.traffic_light = None
        self.auto2.active = False
        
        self._stop_pedestrian(self.Alice)
        # self._stop_pedestrian(self.Barbara)
        # self._stop_pedestrian(self.Carol)
        self._stop_pedestrian(self.Dixy)

        self.agent.clock_status = False
        self.pd_agent.clock_status = False
        QMessageBox.information(self, "Detenido", "El programa se ha detenido.")

    def rotar_imagen(self, pixmap, angulo):
        transform = QtGui.QTransform()
        transform.rotate(angulo)
        return pixmap.transformed(transform, QtCore.Qt.TransformationMode.SmoothTransformation)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PrincipalController()
    window.show()
    sys.exit(app.exec())