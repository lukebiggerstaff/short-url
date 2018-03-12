from django.db import models
from . import base34

class Url(models.Model):

    url = models.URLField(max_length=1000)

    def encoded_url(self):
        return '/' + base34.encode(self.pk)
