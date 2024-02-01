from django.shortcuts import render

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
def resetpassword(request):
    return render(request, "index.html")
def otp(request):
    return render(request, "index.html")
def accountsetup(request):
    return render(request, "index.html")
def verifier(request):
    return render(request, "index.html")
def faqs(request):
    return render(request, "index.html")