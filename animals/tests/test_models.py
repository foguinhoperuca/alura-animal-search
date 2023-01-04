from django.test import TestCase, RequestFactory
from animals.models import Animal


class AnimalModelTestCase(TestCase):
    def setUp(self):
        self.animal = Animal.objects.create(name='Lion', predator='Yes', poisonous='No', domestic='No')

    def test_animal_registered(self):
        """Animal is registered with all features"""
        self.assertEqual(self.animal.name, 'Lion')
        self.assertEqual(self.animal.predator, 'Yes')
        self.assertEqual(self.animal.poisonous, 'No')
        self.assertEqual(self.animal.domestic, 'No')
