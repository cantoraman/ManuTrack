from django.contrib import admin

from .models import Job, Designer, Manufacturer

admin.site.register([Job, Designer, Manufacturer])