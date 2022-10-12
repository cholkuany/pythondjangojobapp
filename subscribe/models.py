from random import choices
from django.db import models

# Create your models here.

NEWSLETTER = [('W', 'Weekly'), ('M', 'Monthly')]

class Subscribe(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    email      = models.CharField(max_length=100)
    option = models.CharField(max_length=2, choices=NEWSLETTER)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"