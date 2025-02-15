# Form implementation generated from reading ui file 'registrar.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from os import path
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form_Registrar(object):
    def setupUi(self, contenedorPrincipal):
        contenedorPrincipal.setObjectName("contenedorPrincipal")
        contenedorPrincipal.resize(900, 600)
        contenedorPrincipal.setStyleSheet(
            "#contenedorPrincipal {\n    background-color: #BFBFBF; /* Gris claro */\n}"
        )
        self.label_7 = QtWidgets.QLabel(parent=contenedorPrincipal)
        self.label_7.setGeometry(QtCore.QRect(340, 30, 261, 31))
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
        base_path = path.dirname(path.abspath(__file__))  
        image_path = path.join(base_path, "../../../resources/images/logo-cafeteria.png")
        self.label_2.setPixmap(QtGui.QPixmap(image_path))

        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.button_cancelar = QtWidgets.QPushButton(parent=contenedorPrincipal)
        self.button_cancelar.setGeometry(QtCore.QRect(700, 490, 101, 34))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(True)
        self.button_cancelar.setFont(font)
        self.button_cancelar.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #2C2C2C;\n"
            "    border: none;\n"
            "    border-radius: 8px;\n"
            "    padding: 5px;\n"
            "    color: white;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #808080; /* Oscurece en hover */\n"
            "}\n"
            "\n"
            ""
        )
        self.button_cancelar.setObjectName("button_cancelar")
        self.button_confirmar = QtWidgets.QPushButton(parent=contenedorPrincipal)
        self.button_confirmar.setGeometry(QtCore.QRect(570, 490, 101, 34))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(True)
        self.button_confirmar.setFont(font)
        self.button_confirmar.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #F28705;\n"
            "    border: none;\n"
            "    border-radius: 8px;\n"
            "    padding: 3px;\n"
            "    color: white;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #A65A18; /* Oscurece en hover */\n"
            "}"
        )
        self.button_confirmar.setObjectName("button_confirmar")
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
        self.cantidad_productos = QtWidgets.QSpinBox(parent=contenedorPrincipal)
        self.cantidad_productos.setGeometry(QtCore.QRect(380, 247, 95, 29))
        self.cantidad_productos.setStyleSheet(
            "QSpinBox {\n    border: none;\n    background-color: #FFFFFFFF;\n}\n"
        )
        self.cantidad_productos.setObjectName("cantidad_productos")
        self.table_lista_productos = QtWidgets.QTableWidget(parent=contenedorPrincipal)
        self.table_lista_productos.setGeometry(QtCore.QRect(50, 210, 428, 311))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.table_lista_productos.setFont(font)
        self.table_lista_productos.setStyleSheet(
            "QTableWidget {\n"
            "    background-color: #FFFFFFFF;\n"
            "    border: 1px solid #F28705;\n"
            "    gridline-color: #2C2C2C;\n"
            "    font-size: 14px;\n"
            "    selection-background-color: #F28705; /* Resaltar selección en naranja */\n"
            "}\n"
            "\n"
            "/* Encabezados de la tabla */\n"
            "QHeaderView::section {\n"
            "    \n"
            "    background-color: white; /* Gris oscuro con opacidad */ /* Fondo oscuro */\n"
            "    color: rgb(44, 44, 44); /* Texto blanco */\n"
            "    padding: 5px;\n"
            "    border: 1px solid #F28705;\n"
            "    font-weight: bold;\n"
            "}\n"
            ""
        )
        self.table_lista_productos.setRowCount(2)
        self.table_lista_productos.setColumnCount(4)
        self.table_lista_productos.setObjectName("table_lista_productos")
        item = QtWidgets.QTableWidgetItem()
        self.table_lista_productos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_lista_productos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_lista_productos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_lista_productos.setHorizontalHeaderItem(3, item)
        self.categoria = QtWidgets.QComboBox(parent=contenedorPrincipal)
        self.categoria.setGeometry(QtCore.QRect(50, 150, 291, 31))
        self.categoria.setStyleSheet(
            "QComboBox {\n"
            "    background-color: #FFFFFF;  /* Fondo blanco */\n"
            "    color: #2C2C2C; /* Texto oscuro */\n"
            "    border: 1px solid #F28705;  /* Borde naranja */\n"
            "    padding: 3px;\n"
            "    font-size: 14px;\n"
            "}\n"
            "\n"
            "QComboBox:hover {\n"
            "    background-color: #F5F5F5; /* Un gris más claro al pasar el cursor */\n"
            "}\n"
            "QComboBox QAbstractItemView {\n"
            "    background-color: #FFFFFF;\n"
            "    selection-background-color: #F28705; /* Fondo naranja al seleccionar */\n"
            "}\n"
            ""
        )
        self.categoria.setObjectName("categoria")
        self.label_9 = QtWidgets.QLabel(parent=contenedorPrincipal)
        self.label_9.setGeometry(QtCore.QRect(520, 120, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(44, 44, 44); \nfont-weight: bold;")
        self.label_9.setObjectName("label_9")
        self.label = QtWidgets.QLabel(parent=contenedorPrincipal)
        self.label.setGeometry(QtCore.QRect(0, 0, 901, 91))
        self.label.setText("")

        image_path = path.join(base_path, "../../../resources/images/header.png")
        self.label.setPixmap(QtGui.QPixmap(image_path))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_10 = QtWidgets.QLabel(parent=contenedorPrincipal)
        self.label_10.setGeometry(QtCore.QRect(50, 120, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(44, 44, 44); \nfont-weight: bold;")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=contenedorPrincipal)
        self.label_11.setGeometry(QtCore.QRect(520, 410, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(44, 44, 44); \nfont-weight: bold;")
        self.label_11.setObjectName("label_11")
        self.table_pedidos = QtWidgets.QTableWidget(parent=contenedorPrincipal)
        self.table_pedidos.setGeometry(QtCore.QRect(520, 150, 328, 221))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.table_pedidos.setFont(font)
        self.table_pedidos.setStyleSheet(
            "QTableWidget {\n"
            "    background-color: #FFFFFFFF;\n"
            "    border: 1px solid #F28705;\n"
            "    gridline-color: #2C2C2C;\n"
            "    font-size: 14px;\n"
            "    selection-background-color: #F28705; /* Resaltar selección en naranja */\n"
            "}\n"
            "\n"
            "/* Encabezados de la tabla */\n"
            "QHeaderView::section {\n"
            "    \n"
            "    background-color: white; /* Gris oscuro con opacidad */ /* Fondo oscuro */\n"
            "    color: rgb(44, 44, 44); /* Texto blanco */\n"
            "    padding: 5px;\n"
            "    border: 1px solid #F28705;\n"
            "    font-weight: bold;\n"
            "}\n"
            ""
        )
        self.table_pedidos.setRowCount(2)
        self.table_pedidos.setColumnCount(3)
        self.table_pedidos.setObjectName("table_pedidos")
        item = QtWidgets.QTableWidgetItem()
        self.table_pedidos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_pedidos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_pedidos.setHorizontalHeaderItem(2, item)
        self.label_3 = QtWidgets.QLabel(parent=contenedorPrincipal)
        self.label_3.setGeometry(QtCore.QRect(670, 390, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(
            "QLabel {\n"
            "    background-color: transparent; /* Fondo completamente transparente */\n"
            "    color: #F28705; /* Naranja vibrante para el texto */\n"
            "    font-size: 24px; /* Tamaño grande para resaltar */\n"
            "    font-weight: bold; /* Negrita para mayor visibilidad */\n"
            "    padding: 5px 0; /* Espaciado arriba y abajo */\n"
            "    border: none;\n"
            "    border-bottom: 2px solid #D17A22; /* Línea inferior naranja */\n"
            "}\n"
            ""
        )
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label.raise_()
        self.fondo_header.raise_()
        self.label_7.raise_()
        self.label_2.raise_()
        self.button_cancelar.raise_()
        self.button_confirmar.raise_()
        self.table_lista_productos.raise_()
        self.cantidad_productos.raise_()
        self.categoria.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.table_pedidos.raise_()
        self.label_3.raise_()

        self.retranslateUi(contenedorPrincipal)
        QtCore.QMetaObject.connectSlotsByName(contenedorPrincipal)

    def retranslateUi(self, contenedorPrincipal):
        _translate = QtCore.QCoreApplication.translate
        contenedorPrincipal.setWindowTitle(_translate("contenedorPrincipal", "Form"))
        self.label_7.setText(_translate("contenedorPrincipal", "Registro de Ventas"))
        self.button_cancelar.setText(_translate("contenedorPrincipal", "Cancelar"))
        self.button_confirmar.setText(_translate("contenedorPrincipal", "Confirmar"))
        item = self.table_lista_productos.horizontalHeaderItem(0)
        item.setText(_translate("contenedorPrincipal", "Producto"))
        item = self.table_lista_productos.horizontalHeaderItem(1)
        item.setText(_translate("contenedorPrincipal", "Precio"))
        item = self.table_lista_productos.horizontalHeaderItem(2)
        item.setText(_translate("contenedorPrincipal", "Stock"))
        item = self.table_lista_productos.horizontalHeaderItem(3)
        item.setText(_translate("contenedorPrincipal", "Cantidad"))
        self.label_9.setText(_translate("contenedorPrincipal", "Listas de productos"))
        self.label_10.setText(_translate("contenedorPrincipal", "Categoría"))
        self.label_11.setText(_translate("contenedorPrincipal", "Total a pagar: S/."))
        item = self.table_pedidos.horizontalHeaderItem(0)
        item.setText(_translate("contenedorPrincipal", "Producto"))
        item = self.table_pedidos.horizontalHeaderItem(1)
        item.setText(_translate("contenedorPrincipal", "Cantidad"))
        item = self.table_pedidos.horizontalHeaderItem(2)
        item.setText(_translate("contenedorPrincipal", "Subtotal"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    contenedorPrincipal = QtWidgets.QWidget()
    ui = Ui_Form_Registrar()
    ui.setupUi(contenedorPrincipal)
    contenedorPrincipal.show()
    sys.exit(app.exec())
