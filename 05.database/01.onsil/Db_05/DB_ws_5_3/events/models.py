from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    participants = models.ManyToManyField('Participant', related_name='events')
    date = models.DateField()
    locations = models.TextField()

    def __str__(self):
        return self.name


class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    registration_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name