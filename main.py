#!/usr/bin/python3
import os
import requests
import google_auth_oauthlib.flow


from flask import Flask
from core.views.generic import IndexView
from catalog.views import *
from catalog.API import APIView

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config["DEBUG"] = True

g_user_endpoint = 'https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token={}'


flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    'google_oauth_secrets.json',
    scopes=[
        'https://www.googleapis.com/auth/userinfo.email',
        'https://www.googleapis.com/auth/userinfo.profile',
        'https://www.googleapis.com/auth/plus.me'
        ]
    )

HOSTNAME = 'catalog.thack.in' if app.env == 'production' else 'localhost:5000'

flow.redirect_uri = 'http://{}/oauth-callback'.format(HOSTNAME)
authorization_url, state = flow.authorization_url(access_type='offline', include_granted_scopes='true')


@app.route('/login')
def login():
    return redirect(authorization_url)


@app.route('/oauth-callback')
def oauth_callback():
        flow.fetch_token(authorization_response=request.url)
        credentials = flow.credentials
        endpoint = g_user_endpoint.format(credentials.token)
        g_user_response = requests.get(endpoint).json()
        a_session['user'] = g_user_response
        return redirect('/categories/')


@app.route('/logout')
def logout():
    if a_session['user'] is not None:
        a_session['user'] = {}
        return redirect('/categories')
    else:
        return "Not Logged In"


# App Routes
app.add_url_rule('/', view_func=IndexView.as_view('index'))


# Category Routes
app.add_url_rule('/add-car',
                 view_func=ItemCreateView.as_view('create_item'))

app.add_url_rule('/my-cars',
                 view_func=ItemListView.as_view('my_items'))

app.add_url_rule(
    '/categories/', view_func=CategoryListView.as_view('show_categories'))

app.add_url_rule('/categories/<pk>',
                 view_func=CategoryDetailView.as_view('show_category_details'))

# Item Routes
app.add_url_rule('/categories/<category_pk>/<pk>',
                 view_func=ItemDetailView.as_view('show_item_details'))

app.add_url_rule('/categories/<category_pk>/add',
                 view_func=ItemCreateView.as_view('add_item'))

app.add_url_rule('/categories/<category_pk>/<pk>/delete',
                 view_func=ItemDeleteView.as_view('delete_item'))

app.add_url_rule('/categories/<category_pk>/<pk>/edit',
                 view_func=ItemUpdateView.as_view('update_item'))


# API Routes
app.add_url_rule(
    '/api/v1/categories/<category_pk>/<pk>', view_func=APIView.as_view('api_list_categories'))


if __name__ == "__main__":
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
