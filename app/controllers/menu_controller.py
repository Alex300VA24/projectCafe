
class MenuController:
    def __init__(self, menu_view, login_view):
        self.menu_view = menu_view
        self.login_view = login_view
        #self.registrar_view = registrar_view
        #self.predicciones_view = predicciones_view
        self.ventanas = {}

    def registrar_ventanas(self, nombre, ventana):
        self.ventanas[nombre] = ventana

    def regresar_login(self):
        """Regresar al login"""
        self.menu_view.close()
        self.login_view.show()

    def abrir_ventana(self, nombre):
        """ Abre una ventana registrada y oculta el menu"""
        if nombre in self.ventanas:
            self.menu_view.close()
            self.ventanas[nombre].show()
