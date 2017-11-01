# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=40)
    type = models.CharField(max_length=1)
    splashImg = models.CharField(max_length=40)
    link = models.URLField(max_length=50)
    skills = models.TextField()
    notes = models.TextField()
    orderID = models.IntegerField()

    def __str__(self):
        return self.title
