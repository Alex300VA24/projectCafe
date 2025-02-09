from PyQt6.QtWidgets import QMainWindow

from views.generated.stock.Ui_Form_Stock import Ui_Form_Stock


class StockView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form_Stock()  # Cargar la interfaz generada
        self.ui.setupUi(self)  # Configurar la interfaz en esta ventana

        self.controller = None


    def set_controller(self, controller):
        """Asigna el controlador y conecta las señales"""
        self.controller = controller
        self.ui.button_cancelar.clicked.connect(self.controller.go_back_to_menu)