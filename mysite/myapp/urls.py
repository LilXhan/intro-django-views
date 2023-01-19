from django.urls import path 
from . import views

urlpatterns = [
    path('myapp/', views.IndexTemplateView.as_view(), name='index'),
    path('form/', views.PersonCreateForm.as_view(), name='form')
]