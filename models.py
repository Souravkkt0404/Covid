from django.db import models

# Create your models here.

class Cars(models.Model):
	company = models.CharField(max_length = 20)
	year = models.IntegerField()
	model_name = models.CharField(max_length=20)

class Employee(models.Model):
	e_name = models.CharField(max_length = 20, primary_key = True)
	e_contact = models.CharField(max_length = 10)

class user_details(models.Model):
	username = models.CharField(max_length = 20, primary_key = True)
	password = models.CharField(max_length = 20)
    
class Image_store(models.Model):
	image = models.ImageField(upload_to = 'newfolder/')
	image_bin = models.BinaryField(blank = True)
