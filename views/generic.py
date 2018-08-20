from flask import request, render_template
from flask.views import View


class LoginView(View):
    methods = ['GET', 'POST']

    def get_objects(self):
        raise NotImplementedError()

    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        if request.method == 'POST':
            print(request.form)
            return self.render_template({})
        context = {'objects': self.get_objects()}
        return self.render_template(context)


class ListView(View):
    def get_objects(self):
        raise NotImplementedError()

    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        print(context)
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        context = {'objects': self.get_objects()}
        return self.render_template(context)
