from django.contrib import admin

#import models
from .models import Guest, Booking

# Register your models here.
class GuestAdmin(admin.ModelAdmin):

    list_display = ("username", "password", "first_name", "last_name")

class BookingAdmin(admin.ModelAdmin):
    list_display = ("get_username", "stay", "check_in", "check_out")

admin.site.register(Guest, GuestAdmin)
admin.site.register(Booking, BookingAdmin)