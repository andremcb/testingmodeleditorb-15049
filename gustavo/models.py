from django.conf import settings
from django.db import models


class Gordinho(models.Model):
    "Generated Model"
    
    MAX_LIMIT = 5
    DATA_PROVIDERS = [
        'http://free.ipwhois.io/json/',
        'http://ip-api.com/json/',
    ]
    
    class Types(models.TextChoices):
        OWNER = 'OW', 'Owner'
        WORKFORCE = 'WF', 'Workforce'
    
    idade = models.CharField(max_length=256,)
    nome = models.CharField(max_length=256, choices=Types.choices, default=Types.OWNER)


# Create your models here.
