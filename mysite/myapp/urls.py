from django.urls import path 
from . import views

urlpatterns = [
    path('myapp/', views.IndexView.as_view(), name='index')
]