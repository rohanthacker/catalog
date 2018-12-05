from .generic import ListView, DetailView
from catalog.session import session
from catalog.models import Category, Item


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'

    # def get_objects(self):
    #     return session.query(Category).distinct().order_by('name')


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'

    def get_context(self, **kwargs):
        super(CategoryDetailView, self).get_context(**kwargs)
        self.context['items'] = session.query(Item).filter_by(category_id=kwargs['pk']).order_by('name').all()
