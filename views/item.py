from .generic import DetailView, CreateView, DeleteView


class ItemDetailView(DetailView):
    template_name = 'item_detail.html'

    def get_object(self, *args, **kwargs):
        return session.query(Item).filter_by(category=kwargs['category_pk'], slug=kwargs['item_pk']).first()


class ItemCreateView(CreateView):
    template_name = 'item_form.html'


class ItemDeleteView(DeleteView):
    template_name = 'item_form.html'
