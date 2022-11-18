from django.test import TestCase, Client
from .views import index_page


class StatisticsTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_functional(self):
        response = self.client.post(path='')
        self.assertEqual(response.status_code,200)
        print (response.context)
