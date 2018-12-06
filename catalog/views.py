from flask import request, redirect, render_template
from flask import session as a_session

from core.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView

from catalog.models import Category, Item
from catalog.session import session


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



class ItemCreateView(CreateView):
    model = Item
    methods = ['GET', 'POST']
    template_name = 'item_create.html'
    redirect_url = 'http://localhost:5000/categories/'

    def get_context(self, **kwargs):
        self.context['object'] = {}
        self.context['category_list'] = session.query(Category).all()

    # def process_form(self, form):
    #     return self.create_object(form)

    def form_valid(self):
        return redirect(self.redirect_url)

    def form_invalid(self, **kwargs):
        self.context['errors'] = 'ALL WRONG'
        self.context['object'] = kwargs['form']
        return render_template(self.template_name, context=self.context)

    def create_object(self, obj):
        _obj = obj.to_dict()
        _obj['created_by'] = a_session['user']['id']
        try:
            item = Item(**_obj)
            session.add(item)
            session.commit()
            return self.form_valid()
        except Exception as e:
            session.rollback()
            raise e

    def dispatch_request(self, **kwargs):
        # Process form for a POST REQUEST
        if request.method == 'POST':
            try:
                return self.create_object(request.form)
            except Exception as e:
                raise e
        # TODO: Remove empty object creation
        # Display form for an authorized GET REQUEST
        elif a_session.get('user') is not None:
            self.get_context(**kwargs)
            return render_template(self.template_name, context=self.context)
        # Redirect to Login
        else:
            return redirect('/login')


class ItemDetailView(DetailView):
    model = Item


class ItemUpdateView(UpdateView):
    methods = ['GET', 'POST']
    model = Item
    template_name = 'item_update.html'

    def get_context(self):
        super(ItemUpdateView, self).get_context(pk=request.view_args['pk'])
        self.context['category_list'] = session.query(Category).all()


class ItemDeleteView(DeleteView):
    model = Item
    redirect_url = '/categories'


class ItemListView(ListView):
    model = Item
    template_name = 'my-cars.html'

    # def get_objects(self):
    #     items = session.query(Item).filter_by(created_by=a_session['user']['id'])
    #     return dict(objects=items)

    # def dispatch_request(self):
    #     return self.render_template(context=self.get_objects())
