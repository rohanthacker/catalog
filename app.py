#!/usr/bin/python3
from flask import Flask
from views.generic import IndexView
from views.auth import LoginView, LogoutView
from views.category import CategoryListView, CategoryDetailView
from views.item import ItemDetailView, ItemCreateView, ItemDeleteView
from views.API import APIView

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config["DEBUG"] = True

# App Routes
app.add_url_rule('/', view_func=IndexView.as_view('index'))

# Auth Routes
app.add_url_rule('/login/', view_func=LoginView.as_view('login'))
app.add_url_rule('/logout/', view_func=LogoutView.as_view('logout'))

# Category Routes
app.add_url_rule(
    '/categories/', view_func=CategoryListView.as_view('show_categories'))

app.add_url_rule('/categories/<category_pk>',
                 view_func=CategoryDetailView.as_view('show_category_details'))

# Item Routes
app.add_url_rule('/categories/<category_pk>/<item_pk>',
                 view_func=ItemDetailView.as_view('show_item_details'))

app.add_url_rule('/categories/<category_pk>/add',
                 view_func=ItemCreateView.as_view('add_item'))

app.add_url_rule('/categories/<category_pk>/<item_pk>/delete',
                 view_func=ItemDeleteView.as_view('delete_item'))

# API Routes
app.add_url_rule(
    '/api/v1/categories/', view_func=APIView.as_view('api_list_categories'))
