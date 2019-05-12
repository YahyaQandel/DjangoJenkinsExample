from django.test import TestCase


class ExampleTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hello_world(self):
        self.assertEqual(1, 1)
