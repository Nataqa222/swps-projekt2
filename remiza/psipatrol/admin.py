from django.contrib import admin
from .models import Firefighter,Firetruck,Squad,FireFighterInSquad

# Register your models here.

admin.site.register(Firefighter)
admin.site.register(Firetruck)
admin.site.register(Squad)
admin.site.register(FireFighterInSquad)