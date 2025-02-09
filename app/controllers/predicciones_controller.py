class PrediccionesController:
    def __init__(self, menu_view, predicciones_view):
        self.predicciones_view = predicciones_view
        self.menu_view = menu_view

    def go_back_to_menu(self):
        """Regresar al menú"""
        self.predicciones_view.close()
        self.menu_view.show()
