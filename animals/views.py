from django.shortcuts import render
from animals.models import Animal


def index(request):
    ctx = {
        'feats': Animal.objects.all()
    }
    return render(request, 'animals/index.html', ctx)
