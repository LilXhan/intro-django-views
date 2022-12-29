from django.urls import path 
from . import views

urlpatterns = [
    path('myapp/', views.index, name='index')
]