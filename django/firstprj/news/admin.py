from django.contrib import admin
from news.models import newss

class newsss(admin.ModelAdmin):
    show=('title','content','img')
admin.site.register(newss,newsss)