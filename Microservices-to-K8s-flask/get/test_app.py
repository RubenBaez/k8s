import unittest

from app import app

class TestConference(unittest.TestCase):

    def test_conference(self):
        # Use Flask's test client for our test.
        self.test_app = app.test_client()

        response = self.test_app.get("192.168.99.100:32339")

        self.assertEquals(response.status, "200 OK")