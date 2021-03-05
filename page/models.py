from django.db import models

# Create your models here.
class DigitData(models.Model):
    digit=models.CharField(max_length=200)
    
class StringData(models.Model):
    string=models.CharField(max_length=200)

class AlphaData(models.Model):
    alpha=models.CharField(max_length=200)
