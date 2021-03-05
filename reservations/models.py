from django.db import models
from django.utils import timezone


class Companies(models.Model):
    company = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.company}"


class Rooms(models.Model):
    room_no = models.CharField(max_length=20)
    room_type = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.room_no}"



class Guest(models.Model):
    registration_no = models.IntegerField()
    name = models.CharField(max_length=40)
    email = models.EmailField()
    passport = models.CharField(max_length=40)
    nationality = models.CharField(max_length=40)
    phone = models.DecimalField(max_digits=15, decimal_places=0)
    category = models.CharField(max_length=40)
    company = models.ForeignKey('Companies', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.email} {self.passport} {self.nationality}"



class Reservations(models.Model):
    guest = models.ForeignKey('Guest', on_delete=models.RESTRICT, null=False)
    room = models.ForeignKey('Rooms', on_delete=models.RESTRICT, null=False)
    checkin_date = models.DateTimeField(default=timezone.now)
    checkout_date = models.DateTimeField(default=timezone.now)
    booking_type = models.CharField(max_length=40)
    meal_plan = models.CharField(max_length=40)
    create_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.guest} {self.room}"


class Invoice(models.Model):
    invoice_no = models.CharField(max_length=10)
    reservation = models.ForeignKey('Reservations', related_name="reservations", on_delete=models.RESTRICT, null=False)
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)
    other_charges = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.invoice_no}"


class Guesthouse(models.Model):
    name = models.CharField(max_length=20)
    capacity = models.DecimalField(max_digits=15, decimal_places=0)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
