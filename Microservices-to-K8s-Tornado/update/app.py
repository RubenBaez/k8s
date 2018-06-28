import tornado.ioloop
import tornado.web
import os.path

from pymongo import MongoClient
from bson.objectid import ObjectId

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

login_db()

class MainHandler(tornado.web.RequestHandler):
    def post(self, objectIde):
        _items = con().coll.find({"_id": ObjectId(objectIde)})
        print(objectIde)
        itemsId = [item for item in _items]
        event=[]
        context=[]
        for i in itemsId:
            event.append(i['event'])
            context.append(i['context'])

        self.render('informacion.html', itemsId=itemsId, event=event, context=context)
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
        key=self.get_argument('id')
        con().coll.update({"_id":ObjectId(key)}, item_doc)

        self.redirect("http://192.168.99.100:31177/gettornado")

settings = {
    "blog_title": u"Datos de Mongo",
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path" : os.path.join(os.path.dirname(__file__), "static"),
    #"ui_modules": {"Entry": EntryModule},
    "xsrf_cookies": False,
}

def make_app():
    return tornado.web.Application([
        (r"/informaciontornado/([^/]+)", MainHandler),
        (r"/actualizartornado", RubenHandler),
    ], debug=True,  **settings)

def main():
    app=make_app()
    return app

app=main()

if __name__=='__main__':
    #app=make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
