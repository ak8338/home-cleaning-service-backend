# bookings/serializers.py

from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        # Prevent double booking at the same time
        if Booking.objects.filter(booking_date=data['booking_date']).exists():
            raise serializers.ValidationError('This time slot is already taken.')
        return data
