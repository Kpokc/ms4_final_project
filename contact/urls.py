from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('contact/sent/', views.sent, name='sent'),
]
