#encoding: utf-8
import os 
import requests

result = requests.get("http://192.168.99.100:30050")

print(result.status_code)

if(result.status_code==200):
	print("Accedido :)")
else:
	print("Algo va mal..")

