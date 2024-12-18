from django.db import models

# Create your models here.
class Features(models.Model):
    Features_Icon=models.CharField(max_length=50)
    Features_Title=models.CharField(max_length=50)
    Features_Description=models.TextField()
    
