from .generic import LoginView, LogoutView
from models.main import User, Item, Category
from models.session import session


class LoginView(LoginView):
    def get_template_name(self):
        return 'login.html'


class LogoutView(LogoutView):
    template_name = 'logout.html'
