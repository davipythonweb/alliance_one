from django.urls import path

from . import views

app_name = 'cars'

urlpatters = [
    path('cars/', views.CarsListAPIView.as_view(),
         name='cars-list'),
]