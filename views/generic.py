import bcrypt
from flask import request, render_template, redirect
from flask.views import View
from models.main import User
from models.session import session
from flask import session as a_session


class TemplateView(View):
    template_name = None

    def render_template(self):
        return render_template(self.template_name)

    def dispatch_request(self):
        self.logout()
        return self.render_template()


class LoginView(View):
    methods = ['GET', 'POST']
    redirect_url = '/categories/'
    template_name = 'login.html'

    def get_user(self):
        return session.query(User).first()

    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context={}):
        return render_template(self.get_template_name(), **context)

    def authenticate(self, username, password):
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


class CreateView(TemplateView):
    pass


class DeleteView(TemplateView):
    pass
