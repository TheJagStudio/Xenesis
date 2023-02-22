from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('app/register', views.registerApp, name="registerApp"),
    path('app/login', views.loginApp, name="loginApp"),
    path('app/otpvalidation', views.otpvalidationApp, name="otpvalidationApp"),
    path('app/accountsetup', views.accountsetupApp, name="accountsetupApp"),
    path('app/resendotp', views.resendotpApp, name="resendotpApp"),
    path('app/forgotpassword', views.forgotpasswordApp, name="forgotpasswordApp"),
    path('app/accountSetup', views.accountSetupApp, name="accountSetupApp"),
    path('app/locationSetter', views.locationSetterApp, name="locationSetterApp"),
    path('app/homeDataFetcher', views.homeDataFetcherApp, name="homeDataFetcherApp"),
    path('app/eventsSearch', views.eventsSearchApp, name="eventsSearchApp"),
    path('app/eventDetailFetcher', views.eventDetailFetcherApp, name="eventDetailFetcherApp"),
    path('app/galleryList', views.galleryListApp, name="galleryListApp"),
    path('app/eventList', views.eventListApp, name="eventListApp"),
]
