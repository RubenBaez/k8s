import tornado.ioloop
import tornado.web
import os.path

from pymongo import MongoClient
from bson.objectid import ObjectId

#global PAG = 1
MONGO_HOST = "192.168.99.100:30820"
MONGO_PORT = 27017
MONGO_DB = "jsondb"
MONGO_USER = "ruben"
MONGO_PASS = "1234"
connection = MongoClient(MONGO_HOST, MONGO_PORT)
db = connection[MONGO_DB]
db.authenticate(MONGO_USER, MONGO_PASS)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        _items = db.coll.find().limit(1000)
        items = [item for item in _items]
        self.render("todo.html", items=items)
        
class RubenHandler(tornado.web.RequestHandler):
    def get(self, param):
        _items = db.coll.find({"_id":ObjectId(param)})
        itemsId = [item for item in _items]
        event=[]
        context=[]
        for i in itemsId:
            event.append(i['event'])
            context.append(i['context'])
        self.render("informacion.html", itemsID=itemsID, event=event, context=context)
        #self.write("Ruben Dario, soy tornado")

class PagHandler(tornado.web.RequestHandler):
    def post(self, param):
        limite = 1000
        PAG = int(param)
        atras=self.get_argument('atras')
        siguiente=self.get_argument('siguiente')
        PAG = PAG - int(atras)
        PAG = PAG + int(siguiente)
        if PAG == 1:
            return self.redirect("http://127.0.0.1:8000/")
        pagination = PAG * limite
        _items = db.coll.find().skip(pagination).limit(limite)
        items = [item for item in _items]
        self.render("pagination.html", items=items, PAG=PAG)

settings = {
    "blog_title": u"Datos de Mongo",
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path" : os.path.join(os.path.dirname(__file__), "static"),
    #"ui_modules": {"Entry": EntryModule},
    "xsrf_cookies": True,
}

def make_app():
    return tornado.web.Application([
        (r"/gettornado", MainHandler),
        (r"/informacion/([^/]+)", RubenHandler),
        (r"/paginacion/([^/]+)", PagHandler),
    ], debug=True,  **settings)

def main():
    app=make_app()
    return app

app = main()

if __name__=='__main__':
    #app=make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()

