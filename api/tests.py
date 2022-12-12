from rest_framework.test import APITestCase

class StatisticsTests(APITestCase):
    def test_api1(self):
        url = 'https://127.0.0.1:8000/api/abc'
        response = self.client.get(url)
        self.assertEqual(response.data, {"symbol_count": {"a": 1, "b": 1, "c": 1}, "str_len": 3, 'original': 'abc', 'changed': 'abc'})

    def test_api2(self):
        url = 'https://127.0.0.1:8000/api/"Привет"'
        response = self.client.get(url)
        self.assertEqual(response.data,
                         {"symbol_count": {"\"": 2, "П": 1, "р": 1, "и": 1, "в": 1, "е": 1, "т": 1}, "str_len": 8,
                          "original": "\"Привет\"", "changed": "«Привет»"})

    def test_api3(self):
        url = 'https://127.0.0.1:8000/api/""'
        response = self.client.get(url)
        self.assertEqual(response.data, {"symbol_count": {"\"": 2}, "str_len": 2, "original": "\"\"", "changed": "«»"})

    def test_api4(self):
        url = 'https://127.0.0.1:8000/api/"'
        response = self.client.get(url)
        self.assertEqual(response.data, {"symbol_count": {"\"": 1}, "str_len": 1, "original": "\"", "changed": "«"})

    def test_api5(self):
        url = 'https://127.0.0.1:8000/api/"Мама" и "папа"'
        response = self.client.get(url)
        self.assertEqual(response.data,
                         {"symbol_count": {"\"": 4, "М": 1, "а": 4, "м": 1, " ": 2, "и": 1, "п": 2}, "str_len": 15,
                          "original": "\"Мама\" и \"папа\"", "changed": "«Мама» и «папа»"})
