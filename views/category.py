from .generic import TemplateView, LoginView, ListView, DetailView
from models.session import session
from models.main import Category, Item


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
