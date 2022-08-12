from django.contrib import admin
 
# add include to the path
from django.urls import path, include
 
# import views from guesthouse folder
from guesthouse import views
 
#necessary for routing
from rest_framework import routers
 
# create a router object
router = routers.DefaultRouter()
 
# register the router
router.register(r'guests',views.GuestView, 'guest')
router.register(r'bookings', views.BookingView, 'booking')
 
urlpatterns = [
    path('admin/', admin.site.urls),

    # when you visit the localhost:8000/api
    # you should be routed to the django Rest framework
    path('api/', include(router.urls))
]