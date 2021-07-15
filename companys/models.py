from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField


class Company(models.Model):
    name_company = models.CharField(max_length=100)
    data_create = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_company

    
    class Meta:
        db_table = 'companys'

