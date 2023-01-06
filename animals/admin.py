from django.contrib import admin
from animals.models import Animal


class ListingAnimal(admin.ModelAdmin):
    list_display = ('id', 'name', 'predator', 'poisonous', 'domestic')
    list_display_links = ('id', 'name')
    ordering = ['name']


admin.site.register(Animal, ListingAnimal)