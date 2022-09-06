from django.contrib import admin
from services.models import service

class seradmin(admin.ModelAdmin):
    display = ("head","desc","read")
admin.site.register(service,seradmin)