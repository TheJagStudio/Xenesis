from django.urls import path

from . import views

urlpatterns = [
    path('events/', views.events, name='events'),
    path('eventsHome/', views.eventsHome, name='eventsHome'),
    path('event/<event>', views.event, name='event'),
    path('addData/', views.addData, name='addData'),
    path('ticketVerifer/<ticketQr>/', views.ticketVerifer, name='ticketVerifer'),
    path('ticketPaymentVerifer/<ticketQr>/', views.ticketPaymentVerifer, name='ticketPaymentVerifer'),
    path('foodCouponVerifer/<ticketQr>/', views.foodCouponVerifer, name='foodCouponVerifer'),
    path('ticketData/<ticketQr>/', views.ticketData, name='ticketData'),
    path('foodCouponData/<ticketQr>/', views.foodCouponData, name='foodCouponData'),
]
