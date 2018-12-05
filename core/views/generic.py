import bcrypt
from flask import request, render_template, redirect
from flask.views import View
from catalog.models import User
from catalog.session import session
from flask import session as a_session


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
        if user:
            return True if self.object.created_by == float(user['id']) else False
        else:
            return False

    def dispatch_request(self, **kwargs):

        if self.check_permissions():
            return self.render_template()
        else:
            return self.render_error(message='Unauthorized Request')


class IndexView(TemplateView):
    template_name = 'index.html'

    def dispatch_request(self):
        if 'username' in a_session:
            return redirect('/categories')
        else:
            return self.render_template()


class LoginView(View):
    methods = ['GET', 'POST']
    redirect_url = '/categories/'
    template_name = 'login.html'

    @staticmethod
    def get_user():
        return session.query(User).first()

    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context={}):
        return render_template(self.get_template_name(), **context)

    def authenticate(self, username, password):
        # TODO: Check creds with DB
        hashed_password = b'$2b$12$Fll4TLljj7dYmJMeC5jb2e5ilmj4JGpkbkiMeQo7tk.vNCe6HVewi'
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            a_session['username'] = username
            a_session['logged_in'] = True
            return True

    def dispatch_request(self):
        if request.method == 'POST':
            if self.authenticate(request.form.get('username'), request.form.get('password')):
                return redirect(self.redirect_url)
        else:
            return self.render_template()


class LogoutView(TemplateView):
    template_name = 'logout.html'

    def dispatch_request(self):
        a_session.clear()
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

    def process_form(self, *args, **kwargs):
        o = session.query(Item).first()
        print(o.id)
        o.name = 'JPL'
        session.commit()

    def dispatch_request(self, **kwargs):
        self.get_context()
        self.context['object'] = self.get_object(pk=kwargs['pk'])
        # Handle Form Update
        if request.method == 'POST':
            self.process_form(form=request.form)
            return redirect('/categories/')
        # Show Form to owner
        else:
            if request.method == 'GET':
                super(UpdateView, self).dispatch_request(**kwargs)
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

        super(DeleteView, self).dispatch_request(**kwargs)
        try:
            self.delete_object()
            return redirect('/categories/{}'.format(kwargs['category_pk']))
        except Exception as e:
            return self.render_error('Error while trying to delete item')
