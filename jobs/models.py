from django.db import models

class Job(models.Model):
    # to make the property
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
