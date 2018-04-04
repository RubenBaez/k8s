import os

from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
from bson.objectid import ObjectId

app=Flask(__name__)

#client=MongoClient('mongodb://172.18.0.2:27017') #usado en docker-compose

#MONGO_HOST = "172.18.0.2"
MONGO_HOST = "192.168.99.100:30820"
MONGO_PORT = 27017
MONGO_DB = "jsondb"
MONGO_USER = "ruben"
MONGO_PASS = "1234"
connection = MongoClient(MONGO_HOST, MONGO_PORT)
db = connection[MONGO_DB]
db.authenticate(MONGO_USER, MONGO_PASS)
#print('----')
#pprint.pprint(db.collection_names())


#db = client.jsondb #usado en docker-compose

@app.route('/')
def todo():
    #_items = db.tododb.find()
    _items = db.coll.find().limit(1000)
    items = [item for item in _items]
    return render_template('todo.html', items=items)

@app.route('/informacion/<objectIde>')
def informacion(objectIde):
    _items = db.coll.find({"_id": ObjectId(objectIde)})
    itemsId = [item for item in _items]
    event=[]
    context=[]
    for i in itemsId:
        event.append(i['event'])
        context.append(i['context'])
    return render_template('informacion.html', itemsId=itemsId, event=event, context=context)

@app.route('/paginacion/<param>', methods=['POST'])
def paginacion(param):
    limite = 1000
    PAG = int(param)
    atras = request.form['atras']
    siguiente = request.form['siguiente']
    PAG = PAG - int(atras)
    PAG = PAG + int(siguiente)
    if PAG == 1:
        return redirect(url_for('todo'))
    paginacion = PAG * limite
    _items = db.coll.find().skip(paginacion).limit(limite)
    items = [item for item in _items]
    return render_template('pagination.html', items=items, PAG=PAG)



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
