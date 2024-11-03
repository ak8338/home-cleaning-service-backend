
from django.db import models
from django.core.exceptions import ValidationError

class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    service_type = models.CharField(max_length=50)
    booking_date = models.DateTimeField()

    def __str__(self):
        return f'{self.full_name} - {self.service_type} on {self.booking_date}'

    # Custom validation to prevent double booking at the same time
    def clean(self):
        if Booking.objects.filter(booking_date=self.booking_date).exists():
            raise ValidationError('This time slot is already booked.')
