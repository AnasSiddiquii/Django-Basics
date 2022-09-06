from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class newss(models.Model):
    title = models.CharField(max_length=50)
    content = HTMLField()
    img=models.FileField(upload_to="news/",max_length=250,null=True,default=None)
    slug = AutoSlugField(populate_from='title',unique=True,null=True,default=None)