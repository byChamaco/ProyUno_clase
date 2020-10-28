# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventPrincipal(object):
    def setupUi(self, ventPrincipal):
        ventPrincipal.setObjectName("ventPrincipal")
        ventPrincipal.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ventPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.lblXesCli = QtWidgets.QLabel(self.centralwidget)
        self.lblXesCli.setGeometry(QtCore.QRect(290, 30, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblXesCli.setFont(font)
        self.lblXesCli.setAutoFillBackground(False)
        self.lblXesCli.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.545, y1:0.482955, x2:0.534091, y2:1, stop:0 rgba(38, 78, 203, 255), stop:1 rgba(255, 255, 255, 255));")
        self.lblXesCli.setAlignment(QtCore.Qt.AlignCenter)
        self.lblXesCli.setObjectName("lblXesCli")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 70, 741, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 250, 741, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lblDni = QtWidgets.QLabel(self.centralwidget)
        self.lblDni.setGeometry(QtCore.QRect(30, 110, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblDni.setFont(font)
        self.lblDni.setObjectName("lblDni")
        self.editDni = QtWidgets.QLineEdit(self.centralwidget)
        self.editDni.setGeometry(QtCore.QRect(110, 110, 171, 20))
        self.editDni.setObjectName("editDni")
        self.lblApellidos = QtWidgets.QLabel(self.centralwidget)
        self.lblApellidos.setGeometry(QtCore.QRect(30, 140, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblApellidos.setFont(font)
        self.lblApellidos.setObjectName("lblApellidos")
        self.editApel = QtWidgets.QLineEdit(self.centralwidget)
        self.editApel.setGeometry(QtCore.QRect(110, 150, 311, 20))
        self.editApel.setObjectName("editApel")
        self.lblNombre = QtWidgets.QLabel(self.centralwidget)
        self.lblNombre.setGeometry(QtCore.QRect(440, 140, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblNombre.setFont(font)
        self.lblNombre.setObjectName("lblNombre")
        self.editNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.editNombre.setGeometry(QtCore.QRect(490, 150, 231, 20))
        self.editNombre.setObjectName("editNombre")
        self.btnAceptar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAceptar.setGeometry(QtCore.QRect(290, 280, 75, 23))
        self.btnAceptar.setObjectName("btnAceptar")
        self.btnSalir = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalir.setGeometry(QtCore.QRect(420, 280, 75, 23))
        self.btnSalir.setObjectName("btnSalir")
        self.lblValidar = QtWidgets.QLabel(self.centralwidget)
        self.lblValidar.setGeometry(QtCore.QRect(300, 100, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblValidar.setFont(font)
        self.lblValidar.setText("")
        self.lblValidar.setObjectName("lblValidar")
        self.lblSexo = QtWidgets.QLabel(self.centralwidget)
        self.lblSexo.setGeometry(QtCore.QRect(30, 190, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblSexo.setFont(font)
        self.lblSexo.setObjectName("lblSexo")
        self.rbtnFemenino = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtnFemenino.setGeometry(QtCore.QRect(110, 200, 91, 21))
        self.rbtnFemenino.setObjectName("rbtnFemenino")
        self.rbtnMasculino = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtnMasculino.setGeometry(QtCore.QRect(210, 200, 91, 21))
        self.rbtnMasculino.setObjectName("rbtnMasculino")
        self.lblMetPagos = QtWidgets.QLabel(self.centralwidget)
        self.lblMetPagos.setGeometry(QtCore.QRect(330, 190, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblMetPagos.setFont(font)
        self.lblMetPagos.setObjectName("lblMetPagos")
        self.chkEfec = QtWidgets.QCheckBox(self.centralwidget)
        self.chkEfec.setGeometry(QtCore.QRect(490, 190, 71, 41))
        self.chkEfec.setObjectName("chkEfec")
        self.chkTarjeta = QtWidgets.QCheckBox(self.centralwidget)
        self.chkTarjeta.setGeometry(QtCore.QRect(580, 190, 71, 41))
        self.chkTarjeta.setObjectName("chkTarjeta")
        self.chkTrans = QtWidgets.QCheckBox(self.centralwidget)
        self.chkTrans.setGeometry(QtCore.QRect(670, 190, 91, 41))
        self.chkTrans.setObjectName("chkTrans")
        ventPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ventPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        ventPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ventPrincipal)
        self.statusbar.setObjectName("statusbar")
        ventPrincipal.setStatusBar(self.statusbar)
        self.actionSalir = QtWidgets.QAction(ventPrincipal)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(ventPrincipal)
        QtCore.QMetaObject.connectSlotsByName(ventPrincipal)

    def retranslateUi(self, ventPrincipal):
        _translate = QtCore.QCoreApplication.translate
        ventPrincipal.setWindowTitle(_translate("ventPrincipal", "Proyecto Uno"))
        self.lblXesCli.setText(_translate("ventPrincipal", "XESTIÓN CLIENTES"))
        self.lblDni.setText(_translate("ventPrincipal", "DNI:"))
        self.lblApellidos.setText(_translate("ventPrincipal", "Apelidos:"))
        self.lblNombre.setText(_translate("ventPrincipal", "Nome:"))
        self.btnAceptar.setText(_translate("ventPrincipal", "Aceptar"))
        self.btnSalir.setText(_translate("ventPrincipal", "Salir"))
        self.lblSexo.setText(_translate("ventPrincipal", "Sexo:"))
        self.rbtnFemenino.setText(_translate("ventPrincipal", "Femenino"))
        self.rbtnMasculino.setText(_translate("ventPrincipal", "Masculino"))
        self.lblMetPagos.setText(_translate("ventPrincipal", "Métodos de Pago:"))
        self.chkEfec.setText(_translate("ventPrincipal", "Efectivo"))
        self.chkTarjeta.setText(_translate("ventPrincipal", "Tarjeta"))
        self.chkTrans.setText(_translate("ventPrincipal", "Transferencia"))
        self.menuArchivo.setTitle(_translate("ventPrincipal", "Archivo"))
        self.actionSalir.setText(_translate("ventPrincipal", "Salir"))
        self.actionSalir.setShortcut(_translate("ventPrincipal", "Alt+S"))
