from django.db import models

# Import the signal handler
class MyModel(models.Model):
    name = models.CharField(max_length=100)