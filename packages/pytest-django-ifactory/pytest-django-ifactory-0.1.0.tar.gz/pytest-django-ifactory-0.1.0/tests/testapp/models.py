"""Django database models for pytest-django-ifactory's unit tests."""

from __future__ import unicode_literals

from django.db import models


class ModelA(models.Model):

    name = models.CharField(max_length=64, unique=True)
    category = models.CharField(max_length=64)
    blank = models.CharField(max_length=64, blank=True)


class ModelB(models.Model):

    name = models.CharField(max_length=64, unique=True)
    required_a = models.ForeignKey(ModelA, on_delete=models.CASCADE)
    nullable_a1 = models.ForeignKey(
        ModelA, on_delete=models.CASCADE, null=True, related_name="+"
    )
    nullable_a2 = models.ForeignKey(
        ModelA, on_delete=models.CASCADE, null=True, related_name="+"
    )
