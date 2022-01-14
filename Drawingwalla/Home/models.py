from django.db import models
from django.db.models.base import Model
# Create your models here.


    

class Artistss(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField(max_length=100)
    city=models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    i_d=models.CharField(max_length=50)
    price=models.IntegerField()
    img1=models.ImageField(upload_to='pics/')
    img2=models.ImageField(upload_to='pics/')
    img3=models.ImageField(upload_to='pics/')
    availaible=models.BooleanField(default=False)

    def _str_(self):
        return self.name
