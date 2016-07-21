from django.db import models

class Products(models.Model):
    product_id = models.IntegerField
    type = models.CharField(max_length=25)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    quantity = models.IntegerField()
    price = models.FloatField()
    picture = models.CharField(max_length=500)
    is_purchased = models.BooleanField(default=False)

    def __str__(self):                                      #what does this do?
        return self.type + ' - ' + self.name

class Cart(models.Model):
    product = models.ForeignKey(Products)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=150)

