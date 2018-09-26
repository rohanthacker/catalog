from .generic import TemplateView, LoginView, ListView, DetailView
from models.main import User, Item, Category
from models.session import session


class LoginView(LoginView):
    def get_template_name(self):
        return 'login.html'


class LogoutView(TemplateView):
    template_name = 'logout.html'


class CategoryListView(ListView):
    template_name = 'category_list.html'

    def get_objects(self):
        return session.query(Category).order_by('name').all()


class CategoryDetailView(DetailView):
    template_name = 'category_detail.html'

    def get_object(self, *args, **kwargs):
        return {
            'slug': kwargs['category_pk'],
            'items': session.query(Item).filter_by(category=kwargs['category_pk']).order_by('name').all()
        }


class ItemDetailView(DetailView):
    template_name = 'item_detail.html'

    def get_object(self, *args, **kwargs):
        return session.query(Item).filter_by(category=kwargs['category_pk'], slug=kwargs['item_pk']).first()
