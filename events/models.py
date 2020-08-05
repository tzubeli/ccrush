from django.db import models

# Create your models here.



class Event(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    event_photo = models.FilePathField(path="/img")
    # subscribers = models.ArrayField()

