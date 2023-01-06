import logging
from django.shortcuts import render
from termcolor import colored
from animals.models import Animal

logger = logging.getLogger(__name__)


def index(request):
    ctx = {
        'feats': None
    }

    if 'search' in request.GET:
        animals = Animal.objects.all()
        searched_animal = request.GET['search']

        # logger.info(f"{len(animals) = }")  # need additional configuration
        logger.warning('Platform is running at risk')
        logger.warning(colored(f"------------ {len(animals) = } ------------", 'yellow'))
        # logger.debug(f'+++++++++++++++++ DEBUG {len(animals) = } +++++++++++++++++')  # need additional configuration

        feats = animals.filter(name__icontains=searched_animal)
        ctx = {
            'feats': feats
        }

    return render(request, 'index.html', ctx)
