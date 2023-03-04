from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('faqs/', views.faqs, name='faqs'),
    path('login/', views.signin, name='signin'),
    path('register/', views.register, name='register'),
    path('accountSetUp/',views.accountSetUp,name="accountSetUp"),
    path('resendOtp/',views.resendOtpWeb,name="resendOtpWeb"),
    path('otpValidation/', views.otpvalidationWeb, name='otpvalidationWeb'),
    path('event/<event>', views.event, name='event'),
    path('404/', views.pageNotFound, name='pageNotFound'),
    path('cart/', views.cart, name='cart'),
    path('logout/', views.signOut, name='signOut'),
    path('ticketVerifer/', views.ticketVerifer, name='ticketVerifer'),
    path('myTicket/', views.myTicket, name='myTicket'),
    path('ticketGenrator/', views.ticketGenrator, name='ticketGenrator'),
    path('addTeamMembers/', views.addTeamMebers, name='addTeamMebers'),
    path('eventConfirmation/', views.eventConfirmation, name='eventConfirmation'),
    path('deleteIT/', views.deleteIT, name='deleteIT'),
]
