import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QApplication
from PyQt6.QtCore import QTimer

from view.Vista import Ui_VistaPrincipal


class PrincipalController(QtWidgets.QMainWindow, Ui_VistaPrincipal):
    def __init__(self, parent=None):
        super(PrincipalController, self).__init__(parent)
        self.setupUi(self)

        self.btn_Iniciar.clicked.connect(self.begin)
        self.btn_Detener.clicked.connect(self.stop)

        self.timer = QTimer()
        self.timer.timeout.connect(self.cambiar_semaforo)

        self.tiempo = 0  
        self.ciclo_duracion = 15 + 7 + 22

        self.auto1_pos_x = 100  
        self.auto2_pos_y = 600

        self.auto1_debe_seguir = False  
        self.auto2_debe_seguir = False  
        self.semaforo1.setPixmap(self.rotar_imagen(QtGui.QPixmap("./img/v.jpg"), 90))

        self.semaforo1_verde = False  # Estado del semáforo 1 (verde o no)
        self.semaforo2_verde = False  # Estado del semáforo 2 (verde o no)

        # Inicialización de las imágenes de los autos
        self.auto1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.auto1.setGeometry(QtCore.QRect(self.auto1_pos_x, 350, 60, 60))
        
        self.auto1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        pixmap = QtGui.QPixmap("./img/auto.png")
        self.auto1.setPixmap(pixmap)
        self.auto1.setMask(pixmap.createMaskFromColor(QtGui.QColor(255, 255, 255), QtCore.Qt.MaskMode.MaskInColor))
        self.auto1.setScaledContents(True)
        self.auto1.setObjectName("auto1")

        self.auto2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.auto2.setGeometry(QtCore.QRect(500, self.auto2_pos_y, 60, 60))

        self.auto2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        pixmap = QtGui.QPixmap("./img/auto.png")
        self.auto2.setPixmap(pixmap)
        self.auto2.setMask(pixmap.createMaskFromColor(QtGui.QColor(255, 255, 255), QtCore.Qt.MaskMode.MaskInColor))

        self.auto2.setPixmap(self.rotar_imagen(QtGui.QPixmap("./img/auto.png"), 270))  
        self.auto2.setScaledContents(True)
        self.auto2.setObjectName("auto2")

    def begin(self):
        self.timer.start(1000) 
        QMessageBox.information(self, "Iniciado", "El programa ha iniciado.")

    def stop(self):
        self.timer.stop()
        QMessageBox.information(self, "Detenido", "El programa se ha detenido.")

    def cambiar_semaforo(self):
        ciclo_actual = self.tiempo % self.ciclo_duracion 

        if ciclo_actual < 15: 
            # Semáforo 1 verde y rotado 90 grados
            self.semaforo1.setPixmap(self.rotar_imagen(QtGui.QPixmap("./img/v.jpg"), 90))
            self.semaforo2.setPixmap(QtGui.QPixmap("./img/r.jpg"))  
            self.semaforo1_verde = True
            self.semaforo2_verde = False

            self.auto1_debe_seguir = False 
            self.mover_auto1()  
            
        elif ciclo_actual < 15 + 7:
            # Semáforo 1 amarillo
            self.semaforo1.setPixmap(self.rotar_imagen(QtGui.QPixmap("./img/a.jpg"), 90))
            self.semaforo2.setPixmap(QtGui.QPixmap("./img/r.jpg"))  
            self.semaforo1_verde = False
            self.semaforo2_verde = False

            self.verificar_auto1() 
            self.mover_auto1()

        elif ciclo_actual < 22 + 15: 
            # Semáforo 2 verde
            self.semaforo1.setPixmap(self.rotar_imagen(QtGui.QPixmap("./img/r.jpg"), 90))
            self.semaforo2.setPixmap(QtGui.QPixmap("./img/v.jpg"))  
            self.semaforo1_verde = False
            self.semaforo2_verde = True

            self.auto2_debe_seguir = False  
            self.mover_auto2()

        else:  # Semáforo en amarillo para auto2
            self.semaforo1.setPixmap(self.rotar_imagen(QtGui.QPixmap("./img/r.jpg"), 90))  
            self.semaforo2.setPixmap(QtGui.QPixmap("./img/a.jpg"))  
            self.semaforo1_verde = False
            self.semaforo2_verde = False

            self.verificar_auto2()  
            self.mover_auto2()

        self.tiempo += 1

    def verificar_auto1(self):
        if 200 <= self.auto1_pos_x <= 700:
            self.auto1_debe_seguir = True  

    def verificar_auto2(self):
        if 220 <= self.auto2_pos_y <= 500:
            self.auto2_debe_seguir = True  

    def mover_auto1(self):  
        if self.semaforo1_verde or self.auto1_debe_seguir:  
            if self.auto1_pos_x < 850:  
                self.auto1_pos_x += 60
            else:
                self.auto1_pos_x = 50  
            self.auto1.move(self.auto1_pos_x, 350)

    def mover_auto2(self):
        if self.semaforo2_verde or self.auto2_debe_seguir:  
            if self.auto2_pos_y > 40: 
                self.auto2_pos_y -= 60
            else:
                self.auto2_pos_y = 700  
            self.auto2.move(500, self.auto2_pos_y)

    def rotar_imagen(self, pixmap, angulo):
        transform = QtGui.QTransform()
        transform.rotate(angulo)
        return pixmap.transformed(transform, QtCore.Qt.TransformationMode.SmoothTransformation)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PrincipalController()
    window.show()
    sys.exit(app.exec())
