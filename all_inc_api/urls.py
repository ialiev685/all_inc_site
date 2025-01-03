from django.urls import path
from . import views

urlpatterns = [
    path("all-countries/", views.get_all_countries),
    path("depart-cities/", views.get_depart_cities),
    path("resorts/", views.get_resorts),
    path("hotel-categories/", views.get_hotel_categories),
    path("hotels/", views.get_hotels),
    path("tour-operators/", views.get_tour_operators),
    path("tour-dates/", views.get_tour_dates),
]
