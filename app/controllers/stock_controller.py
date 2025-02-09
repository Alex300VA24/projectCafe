class StockController:
    def __init__(self, menu_view, stock_view):
        self.stock_view = stock_view
        self.menu_view = menu_view

    def go_back_to_menu(self):
        """Regresar al menú"""
        self.stock_view.close()
        self.menu_view.show()