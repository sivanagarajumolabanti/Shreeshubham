from django.db import models
from datetime import datetime


class Products(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=25)
    Gold = 'Gold'
    Silver = 'Silver'
    PRODUCT_TYPE_CHOICE = (
        (Gold, 'Gold'),
        (Silver, 'Silver')
    )
    product_type = models.CharField(
        max_length=25,
        choices=PRODUCT_TYPE_CHOICE,
        default=Gold,
    )
    date = models.DateTimeField(default=datetime.now(), null=True)
    product_image = models.ImageField(upload_to='', blank=True, null=True)

    def __str__(self):
        return self.name
