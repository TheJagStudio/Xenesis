from django.urls import path

from . import views

urlpatterns = [
    path('events/', views.events, name='events'),
    path('eventsHome/', views.eventsHome, name='eventsHome'),
    path('event/<event>', views.event, name='event'),
]
