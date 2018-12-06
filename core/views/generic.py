from flask import request, render_template, redirect
from flask.views import View
from flask import session as a_session
from catalog.session import session


class TemplateView(View):
    template_name = None
    context = dict()

    def get_context(self, **kwargs):
        return NotImplementedError()

    def render_template(self):
        return render_template(self.template_name, context=self.context)

    def render_error(self, message):
        return render_template('error.html', context={"error": message})

    def dispatch_request(self, **kwargs):
        self.get_context(**kwargs)
        return self.render_template()


class RedirectView(View):
    redirect_url = None

    def dispatch_request(self):
        return redirect(self.redirect_url)


class SingleObjectView(TemplateView):
    model = None
    object = None

    def get_object(self, pk):
        try:
            self.object = session.query(self.model).filter_by(id=pk).first()
        except Exception as e:
            return self.render_error('Failed to get object')


class AuthorizedView(SingleObjectView):

    def check_permissions(self):
        user = a_session.get('user')
        if user and self.object.is_owner(user):
            return True
        else:
            return False

    def dispatch_request(self, **kwargs):
        return self.check_permissions()


class IndexView(TemplateView):
    template_name = 'index.html'

    def dispatch_request(self):
        if 'username' in a_session:
            return redirect('/categories')
        else:
            return self.render_template()


class ListView(TemplateView):
    model = None

    def get_objects(self):
        return session.query(self.model)

    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.template_name, **context)

    def dispatch_request(self):
        context = {'objects': self.get_objects()}
        session.close()
        return self.render_template(context)


class DetailView(TemplateView):
    model = None

    def get_object(self, pk):
        return session.query(self.model).filter_by(id=pk).first()

    def get_context(self, **kwargs):
        self.context['object'] = self.get_object(pk=kwargs['pk'])


class CreateView(TemplateView):

    def get_object(self, pk):
        return session.query(self.model).filter_by(id=pk).first()

    def get_context(self, **kwargs):
        self.context['object'] = self.get_object(pk=kwargs['pk'])


class UpdateView(AuthorizedView, TemplateView):

    def process_form(self, form, *args, **kwargs):
        self.object.name = form['name']
        self.object.price = form['price']
        self.object.condition = form['condition']
        self.object.production_year = form['production_year']
        self.object.category_id = form['category_id']
        session.commit()

    def dispatch_request(self, **kwargs):
        self.get_context()
        self.get_object(pk=kwargs['pk'])
        self.context['object'] = self.object
        # Handle Form Update
        if request.method == 'POST':
            self.process_form(form=request.form)
            return redirect('/categories/')
        # Show Form to owner
        else:
            if request.method == 'GET':
                if super(UpdateView, self).dispatch_request(**kwargs):
                    # Show Form to object owner
                    return self.render_template()
                else:
                    # Show Error to other users
                    return self.render_error('Unauthorized Request')


class DeleteView(AuthorizedView):
    redirect_url = None

    def delete_object(self):
        session.delete(self.object)
        session.commit()

    def dispatch_request(self, **kwargs):

        self.get_object(pk=kwargs['pk'])

        if super(DeleteView, self).dispatch_request(**kwargs):
            try:
                self.delete_object()
                return redirect('/categories/{}'.format(kwargs['category_pk']))
            except Exception as e:
                return self.render_error('Error while trying to delete item')
        else:
            return self.render_error('Unauthorized Request')
