import os

from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
from bson.objectid import ObjectId

app=Flask(__name__)

#client=MongoClient('mongodb://mongo:27017')

#MONGO_HOST = "172.18.0.2"
MONGO_HOST = "192.168.99.100:30820"
MONGO_PORT = 27017
MONGO_DB = "jsondb"
MONGO_USER = "ruben"
MONGO_PASS = "1234"
connection = MongoClient(MONGO_HOST, MONGO_PORT)
db = connection[MONGO_DB]
db.authenticate(MONGO_USER, MONGO_PASS)

#db = client.jsondb

@app.route('/informacion/<objectIde>')
def todo(objectIde):

    _items = db.coll.find({"_id": ObjectId(objectIde)})
    itemsId = [item for item in _items]
    event=[]
    context=[]
    for i in itemsId:
        event.append(i['event'])
        context.append(i['context'])
    return render_template('informacion.html', itemsId=itemsId, event=event, context=context)

@app.route('/informacion/actualizar', methods=['POST'])
def actualizar():

    item_doc={
            'username':request.form['username'],
            'event_source': request.form['event_source'],
            'name':request.form['name'],
            'accept_languaje':request.form['accept_languaje'],
            'time':request.form['time'],
            'agent':request.form['agent'],
            'page':request.form['page'],
            'host':request.form['host'],
            'session':request.form['session'],
            'referer':request.form['referer'],
            'context':{
                'user_id':request.form['user_id'],
                'org_id':request.form['org_id'],
                'course_id':request.form['course_id'],
                'path':request.form['path'],
                },
            'ip':request.form['ip'],
            'event':{
                'course_id':request.form['course_id'],
                'user_id':request.form['user_id'],
                'mode':request.form['mode'],
                },
            'event_type':request.form['event_type']
            }

    key=request.form['id']
    print(key)
    db.coll.update({"_id":ObjectId(key)}, item_doc)
    return redirect("http://192.168.99.100:31805")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
