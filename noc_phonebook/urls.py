from django.urls import path
from . import views

urlpatterns = [
    path('phones/', views.phones, name='Phones Number'),
]