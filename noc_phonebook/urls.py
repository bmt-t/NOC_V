# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.department_list, name='department_list'),
    path('department/<int:id>/', views.department_details, name='department_details'),
    path('issue/<int:id>/', views.issue_details, name='issue_details'),
]
