from .generic import LoginView, ListView
from models.main import User
from models.session import session


class LoginView(LoginView):
    def get_template_name(self):
        return 'login.html'

    def get_objects(self):
        return session.query(User).all()


class CategoryListView(ListView):
    def get_template_name(self):
        return 'users.html'

    def get_objects(self):
        return session.query(User).all()


# class CategoryDetailView(DetailView):

    def get_template_name(self):
        return 'users.html'

    def get_objects(self):
        return session.query(User).all()
