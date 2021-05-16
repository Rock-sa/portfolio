from django.db import models
#create blog
class Blog(models.Model):
    title = models.CharField(max_length=255) #title
    pub_date =  models.DateTimeField() #pubdate
    body = models.TextField() #body
    image = models.ImageField(upload_to='images/')#image
