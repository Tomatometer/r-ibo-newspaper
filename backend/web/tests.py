from django.test import TestCase


class ExampleCase(TestCase):
    def setUp(self):
        self.num = 42

    def test_example(self):
        self.assertEqual(self.num, 420 // 10)
