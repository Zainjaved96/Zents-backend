from django.db import models

# Create your models here.
from django.db import models


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title
