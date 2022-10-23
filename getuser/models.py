from django.db import models


class Chel(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=25)
    phone = models.CharField(max_length=20)
    addr_city = models.CharField(max_length=30)
