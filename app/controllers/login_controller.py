


class LoginController:
    def __init__(self, login_view, menu_view):
        self.login_view = login_view
        self.menu_view = menu_view

    def login(self):
        self.login_view.close()
        self.menu_view.show()
        