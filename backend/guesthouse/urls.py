from django.urls import path

from . import views
from django.contrib import admin

urlpatterns = [
    path("pay/", views.PayView),
    path("findbookings/<str:username>", views.findGuestBookings),
    path("staybookings/", views.findStayBookings),
    path("createreview/", views.createReview),

]