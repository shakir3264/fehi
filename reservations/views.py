from django.shortcuts import render
from django.http import HttpResponse
from django import forms


# Create your views here.
def index(request):
    return render(request, "reservations/index.html")

class NewReservationForm(forms.Form):
    guest = forms.CharField(label="Guest")
    room = forms.CharField()
    checkin_date = forms.DateTimeInput()
    checkout_date = forms.DateTimeField()
    booking_type = forms.CharField()
    meal_plan = forms.CharField()



def NewReservation(request):
    return render(request, "reservations/newreservation.html", {
        "form": NewReservationForm()
    })
