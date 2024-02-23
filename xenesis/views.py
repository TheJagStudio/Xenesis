from django.shortcuts import render

from django.http import HttpResponse
from api.models import Profile, Department, Event, Ticket



def home(request):
    return render(request, "index.html")
def events(request):
    return render(request, "index.html")
def eventDetails(request,event):
    return render(request, "index.html")
def myticket(request):
    return render(request, "index.html")
def aboutus(request):
    return render(request, "index.html")
def login(request):
    return render(request, "index.html")
def register(request):
    return render(request, "index.html")
def otp(request):
    return render(request, "index.html")
def accountsetup(request):
    return render(request, "index.html")
def verifier(request):
    return render(request, "index.html")
def EventTicketVerifer(request):
    return render(request, "index.html")
def TicketPaymentVerifer(request):
    return render(request, "index.html")
def FoodCouponVerifer(request):
    return render(request, "index.html")
def faqs(request):
    return render(request, "index.html")
def forgotpassword(request):
    return render(request, "index.html")
def resetpassword(request):
    return render(request, "index.html")
def eventConfirmation(request):
    return render(request, "index.html")
def eventRegistration(request):
    return render(request, "index.html")
def verifiedTickets(request):
    return render(request, "index.html")




def aluminiFoodCoupon(request,coupon):
    profile = Profile.objects.filter(foodCoupon2=coupon).first()
    if not profile:
        return render(request, "404.html")
    else:
        temp ={}
        temp["id"] = profile.id
        temp["eventName"] = "Food Coupon (24 Feb 2024)"
        temp["isFoodCoupon"] = True
        temp["qrCodeData"] = coupon
        temp["isScanned"] = profile.isScannedCoupon2
        temp["profilePic"] = profile.profilePic
        temp["username"] = profile.user.first_name
        temp["email"] = profile.user.email
        return render(request, "alluminiTicket.html",{"data":temp})
