from datetime import datetime
from lib2to3.pgen2 import token
from turtle import pd
from django.shortcuts import render
from django.http import JsonResponse

# import view sets from the REST framework
from rest_framework import viewsets
 
# import the Serializers from the serializer file
from .serializers import GuestSerializer, BookingSerializer, ReviewSerializer
 
# import the models from the models file
from .models import Guest, Booking, Review

import json
import requests

# Anonymous test key. Replace with your key.
SECRET_KEY = 'sk_test_960bfde0VBrLlpK098e4ffeb53e1'


def PayView(request):
    token = request.GET.get("token", "")
    username = request.GET.get("username", "")
    stay_name = request.GET.get("stay_name", "")
    checkin = request.GET.get("checkIn", "")
    checkout = request.GET.get("checkOut", "")
    total_cost = int(request.GET.get("total_cost", ""))
    num_guests = request.GET.get("num_guests", "")
    num_rooms = request.GET.get("num_rooms", "")

    # convert date strings to date objects
    checkIn = datetime.strptime(checkin, '%d %b %Y')
    checkOut = datetime.strptime(checkout, '%d %b %Y')
    

    # get user instance with given username
    curruser = Guest.objects.get(username=username)

    response = requests.post(
        'https://online.yoco.com/v1/charges/',
        headers={
            'X-Auth-Secret-Key': SECRET_KEY,
        },
        json={
            'token': token,
            'amountInCents': total_cost,
            'currency': 'ZAR',
        },
    )
    # response.status_code will contain the HTTP status code
    if response.status_code == 201:
        # payment success, create booking in database
        b = Booking(
            stay=stay_name,
            check_in=checkIn,
            check_out=checkOut,
            number_guests=num_guests,
            number_rooms=num_rooms,
            user=curruser
        )
        b.save()
        

    output = json.loads(response.text)
    return JsonResponse({'status_code': output})


# create view to find bookings of cretain guest
def findGuestBookings(request, username):
    Bookings = Booking.objects.all()
    output = []

    for booking in Bookings:
        currUser = booking.user.username
        if currUser == username:
            currBooking = {
                "stay": booking.stay,
                "checkin": booking.check_in,
                "checkout": booking.check_out,
                "guests": booking.number_guests,
            }
            output.append(currBooking)

    if output == []:
        return JsonResponse({'bookings': 'no bookings'})

    return JsonResponse({'bookings': output})
 
# view to find bookings of certain stay and order by date
def findStayBookings(request):
    Bookings = Booking.objects.all().order_by('check_in')
    output = []

    for booking in Bookings:
        currBooking = {
            "stay": booking.stay,
            "check_in": booking.check_in,
            "check_out": booking.check_out,
            "guests": booking.number_guests,
        }
        output.append(currBooking)

    if output == []:
        return JsonResponse({'bookings': 'no bookings'})

    return JsonResponse({'bookings': output})


# view to create new review
def createReview(request):
    username = request.GET.get("username", "")
    stay_name = request.GET.get("stay_name", "")
    comment = request.GET.get("comment", "")
    rating = request.GET.get("rating", "")

    # get user instance with given username
    curruser = Guest.objects.get(username=username)

    r = Review(
        comment = comment,
        rating = rating,
        user = curruser,
        stay = stay_name,
    )
    r.save()

    return JsonResponse({'status_code': 200})


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

# create a class for the Review model viewsets
class ReviewView(viewsets.ModelViewSet):
 
    # create a serializer class and
    # assign it to the ReviewSerializer class
    serializer_class = ReviewSerializer
 
    # define a variable and populate it
    # with the Review list objects
    queryset = Review.objects.all()