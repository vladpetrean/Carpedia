# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Car(models.Model):
    manufacturer_name = models.CharField(max_length=256, blank=False)
    model_name = models.CharField(max_length=256, blank=False)
    release_year = models.IntegerField(blank=False)

    class Meta:
        db_table = "car"
