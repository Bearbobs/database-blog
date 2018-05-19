from django.db import models

# Create your models here.
class posts(models.Model):
	author= models.CharField(max_length=30)
	tittle= models.CharField(max_length=100)
	body= models.TextField()
	timestamp= models.DateTimeField()