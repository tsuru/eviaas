import unittest

from evi import api


class APITestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = api.app.test_client()

    def test_service_add(self):
        response = self.api.post("/resources", data={"name": "name", "plan": "basic"})

        self.assertEqual(201, response.status_code)
        self.assertEqual("", response.data)
