class RegistrarController:
    def __init__(self, menu_view, registrar_view):
        self.registrar_view = registrar_view
        self.menu_view = menu_view

    def go_back_to_menu(self):
        """Regresar al menú"""
        self.registrar_view.close()
        self.menu_view.show()
