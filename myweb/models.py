from django.conf import settings
from django.db import models

class FreshType(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.text}'

class Fresh(models.Model):
    freshType = models.ForeignKey(FreshType, on_delete = models.CASCADE)
    freshName = models.CharField(max_length = 200)
    howFresh = models.CharField(max_length = 1000)

    def __str__(self):
        return f'{self.freshType} - {self.freshName} - {self.howFresh}'
