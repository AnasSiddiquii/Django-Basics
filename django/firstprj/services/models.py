from django.db import models

class service(models.Model):
    head = models.CharField(max_length=50)
    desc = models.TextField()
    read = models.CharField(max_length=50)