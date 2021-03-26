from rest_framework import serializers
from .models import Reservations, Invoice

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = ('id', 'guest', 'room', 'checkin_date', 'checkout_date', 'booking_type', 'meal_plan', 'create_at', 'updated_at')


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ('id', 'invoice_no', 'reservation', 'daily_rate', 'other_charges', 'tgst', 'green_tax', 'service_charge', 'total', 'payment_method')
        