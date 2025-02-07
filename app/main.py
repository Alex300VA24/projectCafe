import sys
from PyQt6.QtWidgets import QApplication
from views.main_view import MainView
from controllers.main_controller import MainController


import warnings


warnings.filterwarnings("ignore", category=DeprecationWarning)


def main():
    app = QApplication(sys.argv)

    # Crear la vista y el controlador
    view = MainView() 
    controller = MainController(view)

    # Asignar el controlador a la vista
    view.set_controller(controller)

    # Mostrar la ventana principal
    view.show()


    sys.exit(app.exec())


if __name__ == "__main__":
    main()