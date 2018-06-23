import os
import requests
from pymongo import MongoClient
import time

MONGO_HOST = "192.168.99.100:32339"
MONGO_PORT = 27017
MONGO_DB = "jsondb"
MONGO_USER = "ruben"
MONGO_PASS = "1234"
connection = MongoClient(MONGO_HOST, MONGO_PORT)
db = connection[MONGO_DB]
db.authenticate(MONGO_USER, MONGO_PASS)
lista=[]

def consultas():
	items=db.coll.distinct("username")
	for p in items:
		lista.append(p)
	return lista

def requestMicroservice():
	items = consultas()
	for i in items:
		result = requests.get("http://192.168.99.100:31216/deletetornado/"+i) 
		print(result.status_code)
		if(result.status_code==200):
			print("Borrado :)")
			time.sleep(60)
		else:
			print("Algo va mal..")
			time.sleep(1)
requestMicroservice()
