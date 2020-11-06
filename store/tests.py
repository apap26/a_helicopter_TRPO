from django.test import TestCase
from . import views
# Create your tests here.asdasasd
class operations(TestCase):
    def test_plus(self):
        result = views.brand(1)
        self.assertEqual(-8, result)