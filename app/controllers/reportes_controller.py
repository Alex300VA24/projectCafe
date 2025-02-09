class ReportesController:
    def __init__(self, menu_view, reportes_view):
        self.reportes_view = reportes_view
        self.menu_view = menu_view

    def go_back_to_menu(self):
        """Regresar al menú"""
        self.reportes_view.close()
        self.menu_view.show()