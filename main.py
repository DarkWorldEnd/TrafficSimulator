import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication
from PyQt5.QtCore import QTimer

from model.enumerate.Direction import Direction
from model.enumerate.Color import Color
from model.Agent import Agent
from model.Pedestrian_Agent import Pedestrian_Agent
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
        
        self.auto1 = Vehicle("CAR-X")
        self.auto1.direction = Direction.EAST
        self.auto1.x = 100
        self.auto1.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.auto1.label.setGeometry(QtCore.QRect(self.auto1.x, 350, 60, 60))        
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
        self.auto2.y = 600
        self.auto2.label.setGeometry(QtCore.QRect(500, self.auto2.y, 60, 60))
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
        self.semaforo1.label = aux
        

        aux = self.semaforo2
        self.semaforo2 = TrafficLight("TL-Y", Color.RED)
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

        self.agent = Agent("Agent 1", [self.semaforo1], [self.semaforo2], [self.flecha1], [self.flecha2])
        self.pd_agent = Pedestrian_Agent("Agent 2", [self.peatonal1, self.peatonal3], [self.peatonal2, self.peatonal4])

    def begin(self):
        self.agent.start_clock()
        self.pd_agent.start_clock()
        self.auto1.thread_roll.start()
        self.auto2.thread_roll.start()
        QMessageBox.information(self, "Iniciado", "El programa ha iniciado.")

    def stop(self):
        self.auto1.direction = None
        self.auto1.traffic_light = None

        self.auto2.direction = None
        self.auto2.traffic_light = None
        
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