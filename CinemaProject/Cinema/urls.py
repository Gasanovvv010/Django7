from django.urls import path
from .views import home, movie_list, movie_detail, booking, bookings

urlpatterns = [
    path('', home, name='home'),
    path('movies/', movie_list, name='movies'),
    path('movies/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('bookings/<int:movie_id>/', booking, name='booking'),
    path('bookings/', bookings, name='bookings'),
]