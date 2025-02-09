from PyQt6.QtWidgets import QMainWindow
from views.generated.menu.Ui_Form_Menu import Ui_Form_Menu


class MenuView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form_Menu()  # Cargar la interfaz generada
        self.ui.setupUi(self)  # Configurar la interfaz en esta ventana

        self.controller = None

    def set_controller(self, controller):
        """Conectar el controlador a la vista"""
        self.controller = controller
        self.ui.cerrar_sesion.clicked.connect(self.controller.regresar_login)
        self.ui.button_prediccion.clicked.connect(
            lambda: self.controller.abrir_ventana("predicciones")
        )
        self.ui.button_registrar_ventas.clicked.connect(
            lambda: self.controller.abrir_ventana("registrar")
        )
        self.ui.button_tendencias.clicked.connect(
            lambda: self.controller.abrir_ventana("tendencias")
        )
        self.ui.button_gestionar_stock.clicked.connect(
            lambda: self.controller.abrir_ventana("stock")
        )
        self.ui.button_reportes_ventas.clicked.connect(
            lambda: self.controller.abrir_ventana("reportes")
        )
