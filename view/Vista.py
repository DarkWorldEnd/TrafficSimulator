# Form implementation generated from reading ui file './ui_views/Vista.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VistaPrincipal(object):
    def setupUi(self, VistaPrincipal):
        VistaPrincipal.setObjectName("VistaPrincipal")
        VistaPrincipal.resize(980, 757)
        VistaPrincipal.setStyleSheet("background-color:rgb(255, 255, 255)")
        VistaPrincipal.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(parent=VistaPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.via = QtWidgets.QLabel(parent=self.centralwidget)
        self.via.setGeometry(QtCore.QRect(120, 50, 761, 621))
        self.via.setText("")
        self.via.setPixmap(QtGui.QPixmap("./ui_views\\../img/via.jpg"))
        self.via.setObjectName("via")
        self.btn_Iniciar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_Iniciar.setEnabled(True)
        self.btn_Iniciar.setGeometry(QtCore.QRect(390, 700, 93, 28))
        self.btn_Iniciar.setObjectName("btn_Iniciar")
        self.btn_Detener = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_Detener.setEnabled(True)
        self.btn_Detener.setGeometry(QtCore.QRect(520, 700, 93, 28))
        self.btn_Detener.setObjectName("btn_Detener")
        self.semaforo1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.semaforo1.setGeometry(QtCore.QRect(330, 410, 71, 91))
        self.semaforo1.setText("")
        self.semaforo1.setPixmap(QtGui.QPixmap("./ui_views\\../img/v.jpg"))
        self.semaforo1.setScaledContents(True)
        self.semaforo1.setObjectName("semaforo1")
        self.semaforo2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.semaforo2.setGeometry(QtCore.QRect(570, 450, 61, 91))
        self.semaforo2.setText("")
        self.semaforo2.setPixmap(QtGui.QPixmap("./ui_views\\../img/r.jpg"))
        self.semaforo2.setScaledContents(True)
        self.semaforo2.setObjectName("semaforo2")
        self.flecha1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.flecha1.setGeometry(QtCore.QRect(340, 500, 61, 41))
        self.flecha1.setText("")
        self.flecha1.setPixmap(QtGui.QPixmap("./ui_views\\../img/fv.jpg"))
        self.flecha1.setScaledContents(True)
        self.flecha1.setObjectName("flecha1")
        self.flecha2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.flecha2.setGeometry(QtCore.QRect(580, 540, 51, 41))
        self.flecha2.setText("")
        self.flecha2.setPixmap(QtGui.QPixmap("./ui_views\\../img/fr.jpg"))
        self.flecha2.setScaledContents(True)
        self.flecha2.setObjectName("flecha2")
        VistaPrincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(VistaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(VistaPrincipal)

    def retranslateUi(self, VistaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        VistaPrincipal.setWindowTitle(_translate("VistaPrincipal", "Semáforo"))
        self.btn_Iniciar.setText(_translate("VistaPrincipal", "Iniciar"))
        self.btn_Detener.setText(_translate("VistaPrincipal", "Detener"))
