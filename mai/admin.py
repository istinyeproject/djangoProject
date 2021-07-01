from django.contrib import admin

from .models import Person, Publication

admin.site.register(Person)
admin.site.register(Publication)
