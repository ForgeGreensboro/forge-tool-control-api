from django.test.client import Client
from django.test import SimpleTestCase


class AccessRequestTests(SimpleTestCase):
    def testView(self):
        c = Client()
        response = c.get()
