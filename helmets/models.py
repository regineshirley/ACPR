from django.db import models


class HelmetsM(models.Model):
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    item_number = models.IntegerField()
    price = models.FloatField()
    picture = models.CharField(max_length=1000)

    def __str__(self):
        return self.type + ' - ' + self.name + ' - ' + str(self.price)