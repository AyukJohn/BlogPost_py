from pyexpat import model
from django.db import models

# Create your models here.


class TutorialModel(models.Model):
    title = models.CharField(max_length = 250)
    description = models.TextField(max_length=850)