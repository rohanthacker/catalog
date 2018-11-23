#!/usr/bin/python3
from core.app import app
from core.views.generic import IndexView
from core.views.category import CategoryListView, CategoryDetailView
from core.views.item import ItemDetailView, ItemCreateView, ItemDeleteView, ItemUpdateView
from core.views.API import APIView


# App Routes
app.add_url_rule('/', view_func=IndexView.as_view('index'))


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

app.add_url_rule('/categories/<category_pk>/<item_pk>/edit',
                 view_func=ItemUpdateView.as_view('update_item'))

# API Routes
app.add_url_rule(
    '/api/v1/categories/<category_pk>/<item_pk>', view_func=APIView.as_view('api_list_categories'))
