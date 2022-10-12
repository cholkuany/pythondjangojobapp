from django.db import models

# Create your models here.

class Upload_Image(models.Model):
    image = models.ImageField(upload_to='images')
    description = models.CharField(max_length=100)

class UploadFiles(models.Model):
    file = models.ImageField(upload_to='files')
    description = models.CharField(max_length=100)


