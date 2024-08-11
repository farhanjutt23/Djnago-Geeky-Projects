from django.urls import path
from . import views
urlpatterns = [
    path('ser/',views.serve, name='services'),
]
