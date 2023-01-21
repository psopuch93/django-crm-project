from django.db import models


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=36, blank=True, unique=True)
    tin = models.IntegerField()
    address = models.CharField(max_length=45, blank=True)
    city = models.CharField(max_length=36, blank=True)
    post = models.CharField(max_length=10, blank=True)
    mail = models.EmailField(blank=True)
    phone = models.CharField(max_length=16, blank = True)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(max_length=256, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)