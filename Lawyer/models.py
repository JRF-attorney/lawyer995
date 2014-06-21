from django.db import models


class Lawyer(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    dutyCountyList = models.ManyToManyField("Info.County")

    def __str__(self):
        return self.name