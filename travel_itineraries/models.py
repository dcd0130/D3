from django.db import models


class TravelItinerary(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    destinations = models.ManyToManyField('Destination')

    def __str__(self):
        return self.name


class Destination(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
