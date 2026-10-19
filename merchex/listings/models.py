from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Band (models.Model):
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(max_length=50)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2021)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    #on veut au lieu de object(identifiant) avoir le nom de la band
    def __str__(self):
        return self.name


class Listing(models.Model):
    class Types(models.TextChoices):
        disques = 'Records'
        vetements = 'Clothing'
        affiches = 'Posters'
        divers = 'Miscellanous'

    description = models.fields.CharField(default="c'est un produit", max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(validators=[MinValueValidator(1900),MaxValueValidator(2026)], default=2009)
    tpe = models.fields.CharField(choices = Types.choices, max_length=12)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
