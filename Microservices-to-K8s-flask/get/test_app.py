import unittest

from app import app as a
import app

class TestConference(unittest.TestCase):

    def test_conference(self):
        # Use Flask's test client for our test.
        self.test_app = app.test_client()

        response = self.test_app.get("http://192.168.99.100:32218/")

        self.assertEquals(response.status, "200 OK")

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
        response = result.get("http://192.168.99.100:32218/", content_type='html/text')
        self.assertTrue(b'Informacion Mongo' in response.data)

    def test_item_not_exist(self):
        self.test_app = a.test_client()
        response = self.test_app.get("http://192.168.99.100:32218/404")
        self.assertEqual(response.status_code, 404)