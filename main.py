import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox,QApplication
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
        
 
        self.estado = 0
        
    def begin(self):
        self.timer.start(1000)  
        QMessageBox.information(self, "Iniciado", "El programa ha iniciado.")

    def stop(self):
        self.timer.stop()
        QMessageBox.information(self, "Detenido", "El programa se ha detenido.")


    def cambiar_semaforo(self):
        if self.estado == 0:
            self.semaforo1.setPixmap(QtGui.QPixmap("./ui_views\\../img/r.jpg"))  
            self.semaforo2.setPixmap(QtGui.QPixmap("./ui_views\\../img/v.jpg"))  
            self.estado = 1
        else:
            self.semaforo1.setPixmap(QtGui.QPixmap("./ui_views\\../img/v.jpg"))  
            self.semaforo2.setPixmap(QtGui.QPixmap("./ui_views\\../img/r.jpg"))  
            self.estado = 0

if __name__ == "__main__":
    app = QApplication(sys.argv)  
    window = PrincipalController()  
    window.show()  
    sys.exit(app.exec())  