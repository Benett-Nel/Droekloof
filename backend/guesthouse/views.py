from django.shortcuts import render

# import view sets from the REST framework
from rest_framework import viewsets
 
# import the Serializers from the serializer file
from .serializers import GuestSerializer, BookingSerializer
 
# import the models from the models file
from .models import Guest, Booking
 
# create a class for the Guest model viewsets
class GuestView(viewsets.ModelViewSet):
 
    # create a serializer class and
    # assign it to the GuestSerializer class
    serializer_class = GuestSerializer
 
    # define a variable and populate it
    # with the Guest list objects
    queryset = Guest.objects.all()

# create a class for the Booking model viewsets
class BookingView(viewsets.ModelViewSet):
 
    # create a serializer class and
    # assign it to the BookingSerializer class
    serializer_class = BookingSerializer
 
    # define a variable and populate it
    # with the Booking list objects
    queryset = Booking.objects.all()