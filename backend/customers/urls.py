from django.urls import path

from . import views

app_name = 'customers'

urlpatters = [
    path('customers/', views.CustomerListAPIView.as_view(),
         name='customer-list'),
]