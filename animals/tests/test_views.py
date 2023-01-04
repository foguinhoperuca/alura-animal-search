from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet

class IndexViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory

    def test_index_view_return_animal(self):
        """Index return correct animal?"""
        response = self.client.get('/', {'feats': 'result'})
        self.assertIs(type(response.context['feats']), QuerySet)
