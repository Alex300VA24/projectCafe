class TendenciasController:
    def __init__(self, menu_view, tendencias_view):
        self.tendencias_view = tendencias_view
        self.menu_view = menu_view

    def go_back_to_menu(self):
        """Regresar al menú"""
        self.tendencias_view.close()
        self.menu_view.show()