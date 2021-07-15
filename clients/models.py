from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    name =  models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=9)
    road = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    area_code = models.CharField(max_length=3)
    city = models.CharField(max_length=100)
    data_create = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
       return self.name


    class Meta:
        db_table = 'clients'
        
