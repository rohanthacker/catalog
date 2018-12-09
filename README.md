# Catalog

# Getting Started

The Catalog app, is separated into two modules, core and catalog along with their
responsibilities outlined below.

* **Core**

    Handles all CRUD aspects of the app and provides all generic views.
   

* **Catalog**

    Handles catalog app implementation through core generic views.
    * models.py - Database Models for Catalog Project 

## Install and Deploy

Clone Source Code

`git clone `

#### Install dependencies

* Python3 
    `apt install python3 python3-pip`
    
* Python dependencies
    `pip3 install -r requirements.txt`

* Postgres
    `apt install postgresql`
    
* Gunicorn Server
    `apt install gunicorn`
    
* Setup Database
    Used the SQL Create statements in Tables.sql to created the required tables.
    * Remember to also create users and grant the required access.*
    
* Run Server with 
    `gunicorn -D -b 0.0.0.0:80 wsgi:app`

___


