# views/main_view.py
from PyQt6.QtWidgets import QMainWindow
from views.generated.main_window import Ui_Form_Main  # Importar la interfaz generada

class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form_Main()  # Crear una instancia de la interfaz generada
        self.ui.setupUi(self)      # Configurar la interfaz en esta ventana

        # Inicializar el controlador como None
        self.controller = None

    def set_controller(self, controller):
        """Asignar el controlador y conectar las señales."""
        self.controller = controller
        print('Señal empezada')
        self.ui.pushButton.clicked.connect(self.controller.handle_button_click)
        print('Señal terminada')

    def update_label(self, text):
        """Actualizar la etiqueta con texto proporcionado por el controlador."""
        self.ui.label.setText(text)