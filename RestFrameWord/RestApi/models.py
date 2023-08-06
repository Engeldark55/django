from django.db import models

# Create your models here.
class Programador(models.Model):
    FullName = models.CharField(max_length=50)
    NickName = models.CharField(max_length=50)
    Age = models.PositiveSmallIntegerField()
    Is_Activate = models.BooleanField(default=True)