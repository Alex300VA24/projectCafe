from PyQt6.QtWidgets import QMainWindow

from views.generated.reportes.Ui_Form_Reportes import Ui_Form_Reportes


class ReportesView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form_Reportes()  # Cargar la interfaz generada
        self.ui.setupUi(self)  # Configurar la interfaz en esta ventana

        self.controller = None


    def set_controller(self, controller):
        """Asigna ûel controlador y conecta las señales"""
        self.controller = controller
        self.ui.btn_cancelar.clicked.connect(self.controller.go_back_to_menu)