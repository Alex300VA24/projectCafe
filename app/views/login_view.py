from PyQt6.QtWidgets import QMainWindow
from views.generated.login.Ui_Form_Login import Ui_Form_Login # Importar la interfaz generada


class LoginView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form_Login()  # Crear una instancia de la interfaz generada
        self.ui.setupUi(self)  # Configurar la interfaz en esta ventana
        # Inicializar el controlador como None
        self.controller = None
        

    def set_controller(self, controller):
        """Asignar el controlador y conectar las señales."""
        self.controller = controller
        self.ui.button_login.clicked.connect(self.controller.login)



