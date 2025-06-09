import self
from django.db import models

class Reminder(models.Model):
    REMIND_BY_CHOICES=[
        ('SMS', 'sms'),
        ('EMAIL', 'email')
    ]

    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    remind_by = models.CharField(max_length=10, choices=REMIND_BY_CHOICES)

    def __str__(self):
        return f"{self.message} on {self.date} at {self.time} via {self.remind_by}"