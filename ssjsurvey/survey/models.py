from django.db import models
from datetime import datetime

from customers.models import Customer
from products.models import Products


class Survey(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now(), null=True)
    feedback = models.TextField(blank=True, null=True)

    choice = (('YES', 'YES'), ('NO', 'NO'))
    purchased = models.CharField(max_length=25, choices=choice, default='yes')

    ratings = (('ONE', 'ONE'), ('TWO', 'TWO'), ('THREE', 'THREE'), ('FOUR', 'FOUR'), ('FIVE', 'FIVE'))

    rating = models.CharField(max_length=25, choices=ratings, default='ONE')

    def __str__(self):
        return self.customer.name
