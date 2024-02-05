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
    # web urls
    path('home/', views.home, name='home'),
    path('userDetail/', views.userDetail, name='userDetail'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('login/', views.signin, name='signin'),
    path('register/', views.register, name='register'),
    path('accountSetUp/',views.accountSetUp,name="accountSetUp"),
    path('resendOtp/',views.resendOtpWeb,name="resendOtpWeb"),
    path('otpValidation/', views.otpvalidation, name='otpvalidation'),
    path('404/', views.pageNotFound, name='pageNotFound'),
    path('cart/', views.cart, name='cart'),
    path('logout/', views.signOut, name='signOut'),
    path('myTicket/', views.myTicket, name='myTicket'),
    path('ticketGenerator/', views.ticketGenerator, name='ticketGenerator'),
    path('addTeamMembers/', views.addTeamMebers, name='addTeamMebers'),
    path('eventConfirmation/', views.eventConfirmation, name='eventConfirmation'),
    path('dataOutper/', views.dataOutper, name='dataOutper'),
    path('closeEvents/', views.closeEvents, name='closeEvents'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    path('dbDownload/', views.dbDownload, name='dbDownload'),
    path('checkUserEmail/', views.checkUserEmail, name='checkUserEmail'),
]
