from flask import request, redirect, render_template
from flask import session as a_session

from core.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView

from catalog.models import Category, Item
from catalog.session import session


class CategoryListView(ListView):
    # Display a categories items in a generic list view
    model = Category
    template_name = 'category_list.html'


class CategoryDetailView(DetailView):
    # Display a categories items generic detail view
    model = Category
    template_name = 'category_detail.html'

    def get_context(self, **kwargs):
        super(CategoryDetailView, self).get_context(**kwargs)
        self.context['items'] = session.query(Item).filter_by(category_id=kwargs['pk']).order_by('name').all()


class ItemCreateView(CreateView):
    # Create Item View
    model = Item
    methods = ['GET', 'POST']
    template_name = 'item_create.html'
    redirect_url = '/categories/'

    def get_context(self, **kwargs):
        self.context['object'] = {}
        self.context['category_list'] = session.query(Category).all()


class ItemDetailView(DetailView):
    # Item Detail View
    model = Item


class ItemUpdateView(UpdateView):
    # Item Update View
    methods = ['GET', 'POST']
    model = Item
    template_name = 'item_update.html'

    def get_context(self):
        super(ItemUpdateView, self).get_context(pk=request.view_args['pk'])
        self.context['category_list'] = session.query(Category).all()


class ItemDeleteView(DeleteView):
    # Item Delete View
    model = Item
    redirect_url = '/categories'


class ItemListView(ListView):
    # My Cars View
    model = Item
    template_name = 'my-cars.html'
