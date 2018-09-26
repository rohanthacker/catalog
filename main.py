from flask import Flask
from views.main import LoginView, LogoutView, CategoryListView, CategoryDetailView, ItemDetailView


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# App Routes
# app.add_url_rule('/', view_func=ShowUsers.as_view('show_users'))


# Auth Routes
app.add_url_rule('/login/', view_func=LoginView.as_view('login'))
app.add_url_rule('/logout/', view_func=LogoutView.as_view('logout'))


# Category Routes
app.add_url_rule(
    '/categories/', view_func=CategoryListView.as_view('show_categories'))

app.add_url_rule('/categories/<category_pk>',
                 view_func=CategoryDetailView.as_view('show_category_dets'))


# Item Routes
app.add_url_rule('/categories/<category_pk>/<item_pk>',
                 view_func=ItemDetailView.as_view('show_item_dets'))
