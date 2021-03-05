from django.contrib import admin

from .models import Guest, Companies, Reservations, Invoice, Guesthouse, Rooms


class GuestAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "passport", "nationality")





admin.site.register(Guest, GuestAdmin)

admin.site.register(Companies)
admin.site.register(Rooms)
admin.site.register(Reservations)
admin.site.register(Invoice)
admin.site.register(Guesthouse)