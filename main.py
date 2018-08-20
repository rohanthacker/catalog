from flask import Flask, render_template

from views.main import LoginView, CategoryListView


app = Flask(__name__)


# App Routes
# app.add_url_rule('/', view_func=ShowUsers.as_view('show_users'))
app.add_url_rule('/login/', view_func=LoginView.as_view('login'))
app.add_url_rule(
    '/categories/', view_func=CategoryListView.as_view('show_cat'))
# app.add_url_rule('/categories/:slug',
#                  view_func=ShowUsers.as_view('show_users'))
# app.add_url_rule('/categories/:slug/:item_name',
#                  view_func=ShowUsers.as_view('show_users'))
