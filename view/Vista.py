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
        self.semaforo1.setGeometry(QtCore.QRect(310, 450, 91, 111))
        self.semaforo1.setText("")
        self.semaforo1.setPixmap(QtGui.QPixmap("./ui_views\\../img/v.jpg"))
        self.semaforo1.setScaledContents(True)
        self.semaforo1.setObjectName("semaforo1")
        self.semaforo2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.semaforo2.setGeometry(QtCore.QRect(560, 450, 81, 111))
        self.semaforo2.setText("")
        self.semaforo2.setPixmap(QtGui.QPixmap("./ui_views\\../img/r.jpg"))
        self.semaforo2.setScaledContents(True)
        self.semaforo2.setObjectName("semaforo2")
        VistaPrincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(VistaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(VistaPrincipal)

    def retranslateUi(self, VistaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        VistaPrincipal.setWindowTitle(_translate("VistaPrincipal", "Semáforo"))
        self.btn_Iniciar.setText(_translate("VistaPrincipal", "Iniciar"))
        self.btn_Detener.setText(_translate("VistaPrincipal", "Detener"))
