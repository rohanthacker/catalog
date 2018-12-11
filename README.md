# Catalog

The Catalog app, is separated into two modules, core and catalog along with their
responsibilities outlined below.
* **Core** : Handles all CRUD aspects of the app and provides all generic views.
* **Catalog** : Handles catalog app implementation through core generic views.


## Getting Started

### Install and Deploy
Clone Source Code

`git clone git@github.com:rohanthacker/catalog.git`

### Install dependencies

* Python3 
    `apt install python3 python3-pip`
    
* Python dependencies
    `pip3 install -r requirements.txt`
    
 
 **Skip the next step, if you cloned this repo via git** 
* Database Setup 
    * Create a file called `catalog.db` in the project root.     
    * Use the SQL Create statements in `fixtures.SQL` to created the required tables.
    * Load Category Items from `fixtures.SQL`'

   
* To start the server run the following commands
    ```
    export FLASK_APP=main.py
    export FLASK_ENV=development
    flask run
    ```
  
___


