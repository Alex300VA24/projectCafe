from PyQt6.QtWidgets import QMainWindow

from views.generated.tendencias.Ui_Form_Tendencias import Ui_Form_Tendencias


class TendenciasView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form_Tendencias()  # Cargar la interfaz generada
        self.ui.setupUi(self)  # Configurar la interfaz en esta ventana

        self.controller = None

    def set_controller(self, controller):
        """Asigna el controlador y conecta las señales"""
        self.controller = controller
        self.ui.button_cancelar.clicked.connect(self.controller.go_back_to_menu)
