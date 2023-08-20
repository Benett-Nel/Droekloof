from django.contrib import admin

#import models
from .models import Guest, Booking, Review

# Register your models here.
class GuestAdmin(admin.ModelAdmin):

    list_display = ("username", "password", "first_name", "last_name")

class BookingAdmin(admin.ModelAdmin):
    list_display = ("get_username", "stay", "check_in", "check_out")

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("get_username", "rating", "comment")

admin.site.register(Guest, GuestAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Review, ReviewAdmin)