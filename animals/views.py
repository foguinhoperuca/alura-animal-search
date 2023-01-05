from django.shortcuts import render
from animals.models import Animal


def index(request):
    ctx = {
        'feats': None
    }

    if 'search' in request.GET:
        animals = Animal.objects.all()
        searched_animal = request.GET['search']
        feats = animals.filter(name__icontains=searched_animal)
        ctx = {
            'feats': feats
        }

    return render(request, 'index.html', ctx)
