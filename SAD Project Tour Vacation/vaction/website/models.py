from django.db import models


class Location(models.Model):

	price = models.CharField(max_length=100)
	img = models.ImageField(upload_to='pics')
	day = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	address = models.TextField() 

class Hotel(models.Model):

	price = models.CharField(max_length=100)
	img = models.ImageField(upload_to='pics')
	status = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	address = models.TextField() 	

