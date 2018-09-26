import bcrypt
from flask import request, render_template
from flask.views import View
from models.main import User
from models.session import session
from flask import session as a_session


class TemplateView(View):
    template_name = None

    def logout(self):
        a_session.pop('username', None)
        a_session.pop('logged_in', False)

    def render_template(self):
        return render_template(self.template_name)

    def dispatch_request(self):
        self.logout()
        return self.render_template()


class LoginView(View):
    methods = ['GET', 'POST']

    def get_user(self):
        return session.query(User).first()

    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def authenticate(self, username, password):
        hashed_password = b'$2b$12$Fll4TLljj7dYmJMeC5jb2e5ilmj4JGpkbkiMeQo7tk.vNCe6HVewi'
        if bcrypt.checkpw(password, hashed_password):
            a_session['username'] = username
            a_session['logged_in'] = True

    def dispatch_request(self):
        if request.method == 'POST':
            self.authenticate('rohan', b'6999')
        context = {'objects': []}
        return self.render_template(context)


class ListView(TemplateView):

    def get_objects(self):
        raise NotImplementedError()

    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.template_name, **context)

    def dispatch_request(self):
        context = {'objects': self.get_objects()}
        session.close()
        return self.render_template(context)


class DetailView(TemplateView):

    def dispatch_request(self, *args, **kwargs):
        context = {'object': self.get_object(**kwargs)}
        session.close()
        return render_template(self.template_name, **context)


class CreateView(View):
    pass


class DeleteView(View):
    pass
