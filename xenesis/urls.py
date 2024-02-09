from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from . import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^sitemap\.xml$', serve, {'document_root': 'static/', 'path': 'sitemap.xml'}),
    re_path(r'^robot\.txt$', serve, {'document_root': 'static/', 'path': 'robot.txt'}),
    path('api/', include('api.urls')),
    path('dashboard/', include('admindashboard.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('eventDetails/<event>', views.eventDetails, name='eventDetails'),
    path('register/', views.register, name='register'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('resetpassword/', views.resetpassword, name='resetpassword'),
    path('otp/', views.otp, name='otp'),
    path('events/', views.events, name='events'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('accountsetup/', views.accountsetup, name='accountsetup'),
    path('verifier/', views.verifier, name='verifier'),
    path('EventTicketVerifer/', views.EventTicketVerifer, name='EventTicketVerifer'),
    path('TicketPaymentVerifer/', views.TicketPaymentVerifer, name='TicketPaymentVerifer'),
    path('FoodCouponVerifer/', views.FoodCouponVerifer, name='FoodCouponVerifer'),
    path('eventConfirmation/', views.eventConfirmation, name='eventConfirmation'),
    path('eventRegistration/', views.eventRegistration, name='eventRegistration'),
    path('myticket/', views.myticket, name='myticket'),
    path('myTicket/', views.myticket, name='myticket'),
    path('faqs/', views.faqs, name='faqs'),
]
