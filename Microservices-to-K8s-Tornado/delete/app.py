import tornado.ioloop
import tornado.web
import os.path

from pymongo import MongoClient
from bson.objectid import ObjectId

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
        
        self.render("todo.html")


class RubenHandler(tornado.web.RequestHandler):
    def get(self, param):
        db.coll.remove({"username":param})
        self.redirect("http://192.168.99.100:31136/gettornado")

settings = {
    "blog_title": u"Datos de Mongo",
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path" : os.path.join(os.path.dirname(__file__), "static"),
    #"ui_modules": {"Entry": EntryModule},
    "xsrf_cookies": False,
}

def make_app():
    return tornado.web.Application([
        (r"/deletetornado", MainHandler),
        (r"/deletetornado/([^/]+)", RubenHandler),
    ], debug=True,  **settings)

def main():
    app=make_app()
    return app

app=main()

if __name__=='__main__':
    i#app=make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
