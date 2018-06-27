import os

from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app=Flask(__name__)

def con():
    #MONGO_HOST = "172.18.0.2" pruebas directas con docker de mongo
    MONGO_HOST = "192.168.99.100:32339"
    MONGO_PORT = 27017
    MONGO_DB = "jsondb"
    connection = MongoClient(MONGO_HOST, MONGO_PORT)
    db = connection[MONGO_DB]
    return db

def login_db():
    db = con()
    MONGO_USER = "ruben"
    MONGO_PASS = "1234"
    return db.authenticate(MONGO_USER, MONGO_PASS)

@app.route('/delete')
def todo():
    #_items = db.tododb.find()
    
    return render_template('todo.html')

@app.route('/delete/<name>')
def new(name):

    print(name)
    con().coll.remove({"username":name})

    return redirect("http://192.168.99.100:30050")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
