from django.conf import settings
from django.db import models


class Gordinho(models.Model):
    "Generated Model"
    idade = models.CharField(max_length=256,)
    nome = models.CharField(max_length=256,)


# Create your models here.
