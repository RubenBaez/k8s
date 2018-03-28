import tornado.ioloop
import tornado.web
import os.path

from pymongo import MongoClient
from bson.objectid import ObjectId

MONGO_HOST = "172.18.0.2"
MONGO_PORT = 27017
MONGO_DB = "jsondb"
MONGO_USER = "ruben"
MONGO_PASS = "1234"
connection = MongoClient(MONGO_HOST, MONGO_PORT)
db = connection[MONGO_DB]
db.authenticate(MONGO_USER, MONGO_PASS)

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        self.render("todo.html")
    get = post

class RubenHandler(tornado.web.RequestHandler):
    def post(self):
    	item_doc={
	
            'username':self.get_argument('username'),
            'event_source': self.get_argument('event_source'),
            'name':self.get_argument('name'),
            'accept_languaje':self.get_argument('accept_languaje'),
            'time':self.get_argument('time'),
            'agent':self.get_argument('agent'),
            'page':self.get_argument('page'),
            'host':self.get_argument('host'),
            'session':self.get_argument('session'),
            'referer':self.get_argument('referer'),
            'context':{
                'user_id':self.get_argument('user_id'),
                'org_id':self.get_argument('org_id'),
                'course_id':self.get_argument('course_id'),
                'path':self.get_argument('path'),
                },
            'ip':self.get_argument('ip'),
            'event':{
                'course_id':self.get_argument('course_id'),
                'user_id':self.get_argument('user_id'),
                'mode':self.get_argument('mode'),
                },
            'event_type':self.get_argument('event_type')
            }
    	db.coll.insert(item_doc)

    	self.render("todo.html")

settings = {
    "blog_title": u"Datos de Mongo",
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path" : os.path.join(os.path.dirname(__file__), "static"),
    #"ui_modules": {"Entry": EntryModule},
    "xsrf_cookies": False,
}

def make_app():
    return tornado.web.Application([
        (r"/post", MainHandler),
        (r"/post/new", RubenHandler),
    ], debug=True,  **settings)

def main():
    app=make_app()
    return app

app=main()

if __name__=='__main__':
    i#app=make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()

