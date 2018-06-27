import unittest

from app import app as a
import app

class TestConference(unittest.TestCase):

    def test_conference(self):
        # Use Flask's test client for our test.
        self.test_app = a.test_client()
        response = self.test_app.get("http://192.168.99.100:30050/post")
        self.assertEquals(response.status, "200 OK")

    def test_sending_form(self):
        # Use Flask's test client for our test.
        self.test_app = a.test_client()

        response = self.test_app.post("http://192.168.99.100:30050/post", data={"username":"rubenbaez", 
        "event_source":"server", 
        "name":"rubenbaez", 
        "accept_languaje":"español", 
        "time":"2016-12-15T17:28:39.146372+00:00", 
        "agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4)", 
        "page":"None", 
        "host":"soer.utpl.edu.ec", 
        "session":"287", 
        "referer":"http://soer.utpl.edu.ec/home/", 
        "user_id":258, 
        "org_id":"1241", 
        "course_id":"54123", 
        "path":"/course/course-v1:UTPL+AIRPOLLUTION+2017_ENE", 
        "ip":"172.18.7.142", 
        "mode":"CR-452", 
        "event_type":"/course/course-v1:UTPL+AIRPOLLUTION+2017_ENE" })

    def test_db(self):
        result = app.con()
        result = str(result)
        self.assertEqual(result, "Database(MongoClient(host=['192.168.99.100:32339'], document_class=dict, tz_aware=False, connect=True), 'jsondb')")

    def test_db_name(self):
        result = app.con().name
        self.assertEqual(result, "jsondb")

    def test_login_db(self):
        result = app.login_db()
        self.assertEqual(result, True)

    def test_page_loads(self):
        result = a.test_client(self)
        response = result.get("http://192.168.99.100:30050/post", content_type='html/text')
        self.assertTrue(b'Informacion Mongo' in response.data)

    def test_item_not_exist(self):
        self.test_app = a.test_client()
        response = self.test_app.get("http://192.168.99.100:30050/post/new")
        self.assertEqual(response.status_code, 404)

    def test_home_page_returns_correct_html(self):
        self.test_app = a.test_client()
        response = self.test_app.get("http://192.168.99.100:30050/post")	
        tpl = a.jinja_env.get_template('todo.html')
        self.assertEqual(tpl.render()[:2700],response.get_data(as_text=True)[:2700])

    #prueba en caso de algun texto que NO deba contener el sitio
    '''
    def test_home_page(self):
         self.test_app = a.test_client()
         response = self.test_app.get("http://192.168.99.100:32218")
         self.assertFalse('texto' in response.get_data(as_text=True))
    '''