from django.db import models
from distutils.command.upload import upload
from pyexpat import model
from statistics import mode

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',blank = True)

    def __str__(self):
        return self.product_name