from django.contrib import admin

from .models import Guest, Companies


class GuestAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "passport", "nationality")



admin.site.register(Guest, GuestAdmin)
admin.site.register(Companies)