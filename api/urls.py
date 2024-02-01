from django.urls import path

from . import views

urlpatterns = [
    path('events/', views.events, name='events'),
    path('event/<event>', views.event, name='event'),
]
