from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    dob = models.DateField()
    bio = models.TextField()
    image = models.FilePathField(path="/img")
    video = models.FilePathField(path="/img")
    gender = models.CharField(max_length=50)
    looking_for = models.CharField(max_length=50)
 