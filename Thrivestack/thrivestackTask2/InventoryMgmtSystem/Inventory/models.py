from django.db import models


class Item(models.Model):
    item_name = models.CharField(null=False, max_length=100)
    description = models.CharField(null=False, max_length=200)
    quantity = models.PositiveIntegerField(null=False)
    price = models.PositiveIntegerField(null=False)


