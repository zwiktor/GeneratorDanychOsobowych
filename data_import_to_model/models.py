from django.db import models
from random import randint
from FakePersonGenerator import settings
import csv


class BaseName(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __repr__(self):
        return self.name


class FemaleName(BaseName):
    pass


class FemaleSurname(BaseName):
    pass


class MaleName(BaseName):
    pass


class MaleSurname(BaseName):
    pass


#01-493,Warszawa (Bemowo),Mazowieckie,Andyjska
class Address(models.Model):
    postal_code = models.CharField(max_length=6)
    city = models.CharField(max_length=256)
    region = models.CharField(max_length=64)
    street = models.CharField(max_length=128)


class ImportInfo(models.Model):
    class_name = models.CharField(max_length=64)
    insert_date = models.DateTimeField()
    data_size = models.PositiveIntegerField()
    file = models.FilePathField() # dodać regex wymagający końca ścieżki z .csv