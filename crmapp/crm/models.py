from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=36, blank=True)
    tin = models.CharField(max_length=13, unique=True)
    mail = models.EmailField(blank=True)
    phone = models.CharField(max_length=16, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    street = models.CharField(max_length=36, blank=True)
    city = models.CharField(max_length=36, blank=True)
    apt_number = models.CharField(max_length=6, blank=True)
    is_hq = models.BooleanField(default=False)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                    related_name='customer_id')


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(max_length=256, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE,
                                    related_name='location_id')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='created_by')


class Status(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=36, unique=True)
    value = models.CharField(max_length=36)

    def __str__(self):
        return self.value


