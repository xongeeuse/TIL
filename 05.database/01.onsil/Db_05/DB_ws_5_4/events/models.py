from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    participants = models.ManyToManyField('Participant', related_name='events',  through='Attendance')

    def __str__(self):
        return self.name

class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Attendance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    check_in = models.TimeField()
    check_out = models.TimeField()