from .generic import ListView, DetailView
from catalog.session import session
from catalog.models import Category, Item


class CategoryListView(ListView):
    # Display Category list through generic list view
    model = Category
    template_name = 'category_list.html'


class CategoryDetailView(DetailView):
    # Display a categories items generic detail view
    model = Category
    template_name = 'category_detail.html'

    def get_context(self, **kwargs):
        super(CategoryDetailView, self).get_context(**kwargs)
        self.context['items'] = session.query(Item).filter_by(category_id=kwargs['pk']).order_by('name').all()
