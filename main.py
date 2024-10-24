import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication
from PyQt5.QtCore import QTimer

from model.enumerate.Direction import Direction
from model.enumerate.Color import Color
from model.Agent import Agent
from model.Vehicle import Vehicle
from model.TrafficLight import TrafficLight
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
        
        self.auto1 = Vehicle("ABC123")
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

        self.auto2 = Vehicle("CAR-X")
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
        self.auto2.direction = Direction.NORTH

        aux = self.semaforo1
        self.semaforo1 = TrafficLight("TL-x", Color.GREEN)
        self.semaforo1.label = aux
        

        aux = self.semaforo2
        self.semaforo2 = TrafficLight("TL-Y", Color.RED)
        self.semaforo2.label = aux

        self.semaforo1.add_vehicle_observer(self.auto1)
        self.semaforo2.add_vehicle_observer(self.auto2)

        self.agent = Agent("Agent 1", [self.semaforo1], [self.semaforo2])

    def begin(self):
        self.agent.start_clock()
        self.auto1.rolling = True
        QMessageBox.information(self, "Iniciado", "El programa ha iniciado.")

    def stop(self):
        self.auto1.rolling = False
        self.auto2.rolling = False
        self.agent.clock_status = False
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
