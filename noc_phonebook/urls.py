from django.urls import path
from . import views

urlpatterns = [
    path('', views.vmain, name='main'),
    path('department/', views.vdepartment, name='department'),
    path('department/details/<int:id>', views.vdepartment_detail, name='department detail'),
]