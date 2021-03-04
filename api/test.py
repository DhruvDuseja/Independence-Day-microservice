import importlib
import unittest
import json

app = importlib.import_module("app")
appy = app.app
api_func = app.get_day

class BasicTest(unittest.TestCase):

    def test_landing(self):
        tester = appy.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_no_country_data(self):
        tester = appy.test_client(self)
        response = tester.get('/api/maldives', content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_proper_data(self):
        with appy.app_context():
            tester = appy.test_client(self)
            response = tester.get('/api/india', content_type='application/json')
            with self.subTest():
                self.assertEqual(response.status_code, 200)
            # with self.subTest():
            #     day, _ = app.get_day('india')
            #     data = '{"Day":"august 15","Unicode flag":"\ud83c\uddee\ud83c\uddf3"}'
            #     print(day)
            #     print(type(day))
            #     result = json.dumps(day)
            #     print(result)
            #     self.assertEqual(result, data)


if __name__ == '__main__':
    unittest.main()