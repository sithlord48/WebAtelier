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

        def test_blog_status_code(self):
            result = self.app.get('/blog')
            self.assertEqual(result.status_code, 200)

        def test_contact_status_code(self):
            result = self.app.get('/contact')
            self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()
