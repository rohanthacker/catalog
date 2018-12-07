#!/usr/bin/python3
import json
import requests
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from flask import Flask, session, redirect, request, Response
from flask import session as a_session

from catalog.session import session as db_session
from catalog.models import User

from core.views.generic import IndexView
from core.views.API import APIView
from catalog.views import *

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config["DEBUG"] = True

g_user_endpoint = 'https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token={}'

# For Testing
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    'google_oauth_secrets.json',
    scopes=[
        'https://www.googleapis.com/auth/userinfo.email',
        'https://www.googleapis.com/auth/userinfo.profile',
        'https://www.googleapis.com/auth/plus.me'
        ]
    )

flow.redirect_uri = 'http://localhost:5000/oauth-callback'
authorization_url, state = flow.authorization_url(
    access_type='offline',
    include_granted_scopes='true')


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
        # try:
        #     new_user = User(name=g_user_response['name'],
        #                     email=g_user_response['email'],
        #                     email_verified=g_user_response['verified_email'])
        #     db_session.add(new_user)
        #     db_session.commit()
        #     db_session.close()
        # except Exception as err:
        #     return Response(err)
        # print({
        #     'token': credentials.token,
        #     'refresh_token': credentials.refresh_token,
        #     'token_uri': credentials.token_uri,
        #     'client_id': credentials.client_id,
        #     'client_secret': credentials.client_secret,
        #     'scopes': credentials.scopes
        # })



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