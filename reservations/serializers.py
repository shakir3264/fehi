from rest_framework import serializers
from .models import Reservations

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = ('id', 'guest', 'room', 'checkin_date', 'checkout_date', 'booking_type', 'meal_plan', 'create_at', 'updated_at')
        