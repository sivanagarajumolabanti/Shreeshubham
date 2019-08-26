from django.db import models
from datetime import datetime
from products.models import Products


class Orderquantity(models.Model):
    products = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    order_quantity = models.CharField(max_length=20)

    def __str__(self):
        return self.order_quantity


class Customer(models.Model):
    name = models.CharField(max_length=25)
    mobile = models.CharField(max_length=10, unique=True)
    email_id = models.EmailField(max_length=50, blank=True)
    pincode = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True)
    order_quantity = models.ManyToManyField(Orderquantity, null=True)
    date = models.DateTimeField(default=datetime.now(), null=True)

    def __str__(self):
        return self.name
