
from django.db import models

class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    trainee_id = models.CharField(max_length=50, unique=True)

   