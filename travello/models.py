from django.db import models

# Create your models here.

# for making a database tables we have to change our class
# we have to add


class Destination (models.Model):

    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='travello_img')
    offer = models.BooleanField(default=False)


1
