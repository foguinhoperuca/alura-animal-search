# import os, django
# from animals.models import Animal

list_animals = [
    {'name': 'urso', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'javali', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'búfalo', 'predator': 'No', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'guepardo', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'molusco', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'caranguejo', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'lagostim', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'corvo', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'golfinho', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'pomba', 'predator': 'No', 'poisonous': 'No', 'domestic': 'Yes'},
    {'name': 'pato', 'predator': 'No', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'elefante', 'predator': 'No', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'flamingo', 'predator': 'No', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'pulga', 'predator': 'No', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'rã', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'morcego-da-fruta', 'predator': 'No', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'girafa', 'predator': 'No', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'mosquito', 'predator': 'No', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'bode', 'predator': 'No', 'poisonous': 'No', 'domestic': 'Yes'},
    {'name': 'gorila', 'predator': 'No', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'gaivota', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'hadoque', 'predator': 'No', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'hamster', 'predator': 'No', 'poisonous': 'No', 'domestic': 'Yes'},
    {'name': 'falcão', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'abelha', 'predator': 'No', 'poisonous': 'Yes', 'domestic': 'Yes'},
    {'name': 'mosca', 'predator': 'No', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'joaninha', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'leopardo', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'leão', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'lagosta', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'lince', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'salamandra', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'polvo', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'gambá', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'órix', 'predator': 'No', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'avestruz', 'predator': 'No', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'periquito', 'predator': 'No', 'poisonous': 'No', 'domestic': 'Yes'},
    {'name': 'pinguim', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'faisão', 'predator': 'No', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'pique', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'piranha', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'ornitorrinco', 'predator': 'Yes', 'poisonous': 'Yes', 'domestic': 'No'},
    {'name': 'doninha', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'pónei', 'predator': 'No', 'poisonous': 'No', 'domestic': 'Yes'},
    {'name': 'toninha', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'puma', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'gato', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'Yes'},
    {'name': 'guaxinim', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'rena', 'predator': 'No', 'poisonous': 'No', 'domestic': 'Yes'},
    {'name': 'ema', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'escorpião', 'predator': 'Yes', 'poisonous': 'Yes', 'domestic': 'No'},
    {'name': 'cavalo marinho', 'predator': 'No', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'leão marinho', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'verme', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'lesma', 'predator': 'No', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'pardal', 'predator': 'No', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'esquilo', 'predator': 'No', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'estrela do Mar', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'arraia', 'predator': 'Yes', 'poisonous': 'Yes', 'domestic': 'No'},
    {'name': 'cisne', 'predator': 'No', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'cupim', 'predator': 'No', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'sapo', 'predator': 'No', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'tartaruga', 'predator': 'No', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'tuatara', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'atum', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'abutre', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'vespa', 'predator': 'No', 'poisonous': 'Yes', 'domestic': 'No'},
    {'name': 'lobo', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'minhoca', 'predator': 'No', 'poisonous': 'No', 'domestic': 'No'},
    {'name': 'Lion', 'predator': 'Yes', 'poisonous': 'No', 'domestic': 'No'}
]

import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from animals.models import Animal

def generate_animals():
    for animal in list_animals:
        a = Animal(name=animal['name'], predator=animal['predator'], poisonous=animal['poisonous'],
                   domestic=animal['domestic'])
        a.save()


generate_animals()
print(f'#{len(list_animals)} Animals generated...')
