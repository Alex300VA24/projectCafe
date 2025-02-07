# controllers/main_controller.py
class MainController:
    def __init__(self, view):
        self.view = view

    def handle_button_click(self):
        """Manejar el clic del botón."""
        print("Botón clicado")
        self.view.update_label("¡Botón clicado!")