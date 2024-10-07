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

   
        self.auto1_pos_x = 50  
        self.auto2_pos_y = 700 

  
        self.auto1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.auto1.setGeometry(QtCore.QRect(self.auto1_pos_x, 350, 40, 40))
        self.auto1.setPixmap(QtGui.QPixmap("./img/auto.jpg"))
        self.auto1.setScaledContents(True)
        self.auto1.setObjectName("auto1")

        self.auto2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.auto2.setGeometry(QtCore.QRect(500, self.auto2_pos_y, 40, 40))
        self.auto2.setPixmap(self.rotar_imagen(QtGui.QPixmap("./img/auto.jpg"), 270))  
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
            self.semaforo1.setPixmap(QtGui.QPixmap("./ui_views\\../img/v.jpg"))  
            self.semaforo2.setPixmap(QtGui.QPixmap("./ui_views\\../img/r.jpg"))  

            self.mover_auto1()  
            
        elif ciclo_actual < 15 + 7: 
            self.semaforo1.setPixmap(QtGui.QPixmap("./ui_views\\../img/a.jpg")) 
            self.semaforo2.setPixmap(QtGui.QPixmap("./ui_views\\../img/r.jpg"))  

        elif ciclo_actual <  22 + 15:  
            self.semaforo1.setPixmap(QtGui.QPixmap("./ui_views\\../img/r.jpg")) 
            self.semaforo2.setPixmap(QtGui.QPixmap("./ui_views\\../img/v.jpg")) 
            self.mover_auto2() 

        else:  
            self.semaforo1.setPixmap(QtGui.QPixmap("./ui_views\\../img/r.jpg"))  
            self.semaforo2.setPixmap(QtGui.QPixmap("./ui_views\\../img/a.jpg"))  
        self.tiempo += 1


    def mover_auto1(self):
        
        if self.auto1_pos_x < 2000:  
            self.auto1_pos_x += 30
            self.auto1.move(self.auto1_pos_x, 350)

    def mover_auto2(self):
        
        if self.auto2_pos_y > 300: 
            self.auto2_pos_y -= 30
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
