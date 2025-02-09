import sys
from PyQt6.QtWidgets import QApplication

from views.login_view import LoginView
from views.menu_view import MenuView
from views.registrar_view import RegistrarView
from views.predicciones_view import PrediccionesView
from views.tendencias_view import TendenciasView
from views.reportes_view import ReportesView
from views.stock_view import StockView

from controllers.login_controller import LoginController
from controllers.menu_controller import MenuController
from controllers.registrar_controller import RegistrarController
from controllers.predicciones_controller import PrediccionesController
from controllers.tendencias_controller import TendenciasController
from controllers.reportes_controller import ReportesController
from controllers.stock_controller import StockController



def main():
    app = QApplication(sys.argv)

    # Crear vistas
    login_view = LoginView()
    menu_view = MenuView()
    registrar_view = RegistrarView()
    stock_view = StockView()
    reportes_view = ReportesView()
    predicciones_view = PrediccionesView()
    tendencias_view = TendenciasView()

    # Crear controladores y asignarlos a las vistas
    login_controller = LoginController(login_view, menu_view)
    menu_controller = MenuController(menu_view, login_view)
    registrar_controller = RegistrarController(menu_view, registrar_view)
    predicciones_controller = PrediccionesController(menu_view, predicciones_view)
    tendencias_controller = TendenciasController(menu_view, tendencias_view)
    reportes_controller = ReportesController(menu_view, reportes_view)
    stock_controller = StockController(menu_view, stock_view)
    
    # Registrar las ventanas en el menu
    menu_controller.registrar_ventanas('registrar', registrar_view)
    menu_controller.registrar_ventanas('predicciones', predicciones_view)
    menu_controller.registrar_ventanas('tendencias', tendencias_view)
    menu_controller.registrar_ventanas('reportes', reportes_view)
    menu_controller.registrar_ventanas('stock', stock_view)

    # Conectar las vistas con los controladores
    login_view.set_controller(login_controller)
    menu_view.set_controller(menu_controller)
    registrar_view.set_controller(registrar_controller)
    predicciones_view.set_controller(predicciones_controller)
    tendencias_view.set_controller(tendencias_controller)
    reportes_view.set_controller(reportes_controller)
    stock_view.set_controller(stock_controller)


    # Mostrar la ventana de login al inicio
    login_view.show()

    # Ejecutar la aplicación
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
