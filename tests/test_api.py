import unittest
import json
import os

from evi import api


class APITestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = api.app.test_client()

    def test_service_add(self):
        response = self.api.post("/resources", data={"name": "name", "plan": "basic"})

        self.assertEqual(201, response.status_code)
        self.assertEqual("", response.data)

    def test_remove_instance(self):
        response = self.api.delete("/resources/myinstance")

        self.assertEqual(200, response.status_code)
        self.assertEqual("", response.data)

    def test_unbind(self):
        response = self.api.delete("/resources/myinstance/hostname/0.0.0.0")

        self.assertEqual(200, response.status_code)
        self.assertEqual("", response.data)

    def test_bind(self):
        os.environ["EVI_ENVIRONS"] = '{"KEY": "MYKEY"}'
        response = self.api.post("/resources/myinstance", data={"hostname": "something.tsuru.io"})

        self.assertEqual(201, response.status_code)

        expected = {"KEY": "MYKEY"}
        result = json.loads(response.data)
        self.assertDictEqual(expected, result)
