#encoding: utf-8
import requests
import os

result = requests.post("http://192.168.99.100:30827/posttornado/new", data={"username":"rubenbaez", "event_source":"server", "name":"rubenbaez", "accept_languaje":"español", "time":"2016-12-15", "agent":"Mozilla/5.0 (Macintosh; Intel Mac OS)", "page":"None", "host":"soer.utpl.edu.ec", "session":"287", "referer":"http://soer.utpl.edu.ec/home/", "user_id":258, "org_id":"1241", "course_id":"54123", "path":"/course/course-v1", "ip":"172.18.7.142", "mode":"CR-452", "event_type":"/course/course-v1" })

print(result.status_code)

if (result.status_code==200):
	print("Accedido :)")
else:
	print("Algo va mal..")

