import unittest
from atelier.main import app


class TestView(unittest.TestCase):
        def setUp(self):
            app.config['TESTING'] = True
            self.app = app.test_client()

        def tearDown(self):
            pass

        def test_sanity(self):
            self.assertEqual(2, 2)

        def test_home_status_code(self):
            result = self.app.get('/')
            self.assertEqual(result.status_code, 200)

        def test_about_status_code(self):
            result = self.app.get('/about')
            self.assertEqual(result.status_code, 200)

        def test_contact_status_code(self):
            result = self.app.get('/contact')
            self.assertEqual(result.status_code, 200)

        def test_download_status_code(self):
            result = self.app.get('/download')
            self.assertEqual(result.status_code, 200)

        def test_documentation_status_code(self):
            result = self.app.get('/documenation')
            self.assertEqual(result.status_code, 200)

        def test_atelier_status_code(self):
            result = self.app.get('/documentation/atelier')
            self.assertEqual(result.status_code, 200)

        def test_atcore_status_code(self):
            result = self.app.get('/documentation/atcore')
            self.assertEqual(result.status_code, 200)

        def test_supportus_status_code(self):
            result = self.app.get('/supportus')
            self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()
