# Form implementation generated from reading ui file 'views/ui/predicciones.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from os import path
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form_Predicciones(object):
    def setupUi(self, contenedorPrincipal):
        contenedorPrincipal.setObjectName("contenedorPrincipal")
        contenedorPrincipal.resize(900, 600)
        contenedorPrincipal.setStyleSheet(
            "#contenedorPrincipal {\n    background-color: #BFBFBF; /* Gris claro */\n}"
        )
        self.label_7 = QtWidgets.QLabel(parent=contenedorPrincipal)
        self.label_7.setGeometry(QtCore.QRect(320, 30, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_2 = QtWidgets.QLabel(parent=contenedorPrincipal)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 101, 81))
        self.label_2.setText("")
        ruta_base = path.dirname(path.abspath(__file__))
        ruta = path.join(ruta_base, '../../../resources/images/logo-cafeteria.png')
        self.label_2.setPixmap(QtGui.QPixmap(ruta))

        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.fondo_header = QtWidgets.QWidget(parent=contenedorPrincipal)
        self.fondo_header.setGeometry(QtCore.QRect(-5, 0, 911, 91))
        self.fondo_header.setStyleSheet(
            "QWidget {    \n"
            "    background-color: rgba(44, 44, 44, 200); /* Gris oscuro con opacidad */\n"
            "\n"
            "    padding: 20px; /* Espaciado interno */\n"
            "    border: 1px solid #F28705; /* Borde sutil naranja */\n"
            "    box-shadow: 3px 3px 15px rgba(0, 0, 0, 100); /* Sombra para efecto flotante */\n"
            "}\n"
            ""
        )
        self.fondo_header.setObjectName("fondo_header")
        self.label = QtWidgets.QLabel(parent=contenedorPrincipal)
        self.label.setGeometry(QtCore.QRect(0, 0, 901, 91))
        self.label.setText("")
        ruta = path.join(ruta_base, '../../../resources/images/header.png')
        self.label.setPixmap(QtGui.QPixmap(ruta))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.button_cancelar = QtWidgets.QPushButton(parent=contenedorPrincipal)
        self.button_cancelar.setGeometry(QtCore.QRect(740, 530, 75, 24))
        self.button_cancelar.setObjectName("button_cancelar")
        self.label.raise_()
        self.fondo_header.raise_()
        self.label_7.raise_()
        self.label_2.raise_()
        self.button_cancelar.raise_()

        self.retranslateUi(contenedorPrincipal)
        QtCore.QMetaObject.connectSlotsByName(contenedorPrincipal)

    def retranslateUi(self, contenedorPrincipal):
        _translate = QtCore.QCoreApplication.translate
        contenedorPrincipal.setWindowTitle(_translate("contenedorPrincipal", "Form"))
        self.label_7.setText(_translate("contenedorPrincipal", "Predicción de Ventas"))
        self.button_cancelar.setText(_translate("contenedorPrincipal", "Cancelar"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    contenedorPrincipal = QtWidgets.QWidget()
    ui = Ui_Form_Predicciones()
    ui.setupUi(contenedorPrincipal)
    contenedorPrincipal.show()
    sys.exit(app.exec())
