from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animals.models import Animal


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory
        self.animal = Animal.objects.create(name='Calopsita', predator='No', poisonous='No', domestic='Yes')

    def test_index_view_return_animal(self):
        """Index return correct animal?"""
        response = self.client.get('/', {'search': 'Calopsita'})
        feat_searched = response.context['feats']
        self.assertIs(type(response.context['feats']), QuerySet)
        self.assertEqual(feat_searched[0].name, 'Calopsita')
