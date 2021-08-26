from django.db import models

# Create your models here.

class newu(models.Model):
    fname = models.CharField(max_length=255,default='fname')
    uname = models.CharField(max_length=255,default='uname')
    email = models.EmailField(unique=True)
    img = models.FileField(upload_to="img/",default="20191207_081057.jpg")