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

* Postgres
    `apt install postgresql`
    
* Gunicorn Server
    `apt install gunicorn`
    
* Setup Database
    `postgres`
    
* Run Server with 
    `EXPORT FLASK_APP=main.py`
    `flask run`

___
