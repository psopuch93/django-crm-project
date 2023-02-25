from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=36, blank=True, unique=True)
    tin = models.IntegerField()
    address = models.CharField(max_length=45, blank=True)
    city = models.CharField(max_length=36, blank=True)
    post = models.CharField(max_length=10, blank=True)
    mail = models.EmailField(blank=True)
    phone = models.CharField(max_length=16, blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(max_length=256, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                    related_name='comments')


class Status(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=36, unique=True)
    value = models.CharField(max_length=36)

    def __str__(self):
        return self.value


class Headquarter(models.Model):
    id = models.AutoField(primary_key=True)
    street = models.CharField(max_length=36, blank=True)
    city = models.CharField(max_length=36, blank=True)
    apt_number = models.CharField(max_length=6, blank=True)
