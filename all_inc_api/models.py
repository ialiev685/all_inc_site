from django.db import models


# Create your models here.


class CountryModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    alias = models.CharField(max_length=50, blank=True)
    flags = models.IntegerField(blank=True)
    has_tickets = models.BooleanField(blank=True)
    hotel_is_not_in_stop = models.BooleanField(blank=True)
    is_visa = models.BooleanField(blank=True)
    is_pro_visa = models.BooleanField(blank=True)
    original_name = models.CharField(max_length=100, blank=True)
    rank = models.IntegerField(blank=True)
    tickets_included = models.BooleanField(blank=True)
