from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('api/', include('api.urls')),
    path('dashboard/', include('admindashboard.urls')),
    path('api/', include('web.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('eventDetails/<event>', views.eventDetails, name='eventDetails'),
    path('myticket/', views.myticket, name='myticket'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('login/', views.login, name='login'),
    path('resetpassword/', views.resetpassword, name='resetpassword'),
    path('otp/', views.otp, name='otp'),
    path('accountsetup/', views.accountsetup, name='accountsetup'),
    path('verifier/', views.verifier, name='verifier'),
    path('faqs/', views.faqs, name='faqs'),
]
