from django.contrib import admin
from .models import State, Headline, Companines,Cities, MagazineCategory, Magazine, SundayMagazine
from django.db import models

# Register your models here

admin.site.register(State)
admin.site.register(Headline)
admin.site.register(Companines)
admin.site.register(Cities)
admin.site.register(MagazineCategory)
admin.site.register(Magazine)
admin.site.register(SundayMagazine)