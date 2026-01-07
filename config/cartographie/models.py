from django.contrib.gis.db import models
from django.contrib.gis.geos import point

class Parcelle (models.Model):
    numparcelle=models.CharField(max_length=100, primary_key=True)
    usage=models.CharField(max_length=100)
    superficie=models.FloatField()
    proprietaire=models.CharField(max_length=255)
    contact=models.CharField(max_length=100)
    geom=models.PolygonField(srid=4326)

def __str__(self):
    return self.numparcelle