from django.http import HttpResponse
from .models import Profile, Department, Event, Ticket, Notifications, Gallery
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import json
import re
import requests
import random
from django.views.decorators.csrf import csrf_exempt


def index(request):
    objects = Profile.objects.all().first()
    name = objects.user.get_full_name()
    profilePic = objects.profilePic
    location = objects.location
    phone = objects.phone
    otp = objects.otp
    isVolunteer = objects.isVolunteer
    isOrganiser = objects.isOrganiser
    isAccountSetup = objects.isAccountSetup
    data = {
        "name": name,
        "profilePic": profilePic,
        "location": location,
        "phone": phone,
        "otp": otp,
        "isVolunteer": isVolunteer,
        "isOrganiser": isOrganiser,
        "isAccountSetup": isAccountSetup
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


def check(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False


@csrf_exempt
def loginApp(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            email = body['email']
            password = body['password']
            try:
                username = User.objects.filter(email=email).first().username
                user = authenticate(username=username, password=password)
                if user is not None:
                    profile = Profile.objects.filter(user=user).first()
                    isVerified = profile.isVerified
                    isAccountSetup = profile.isAccountSetup
                    if isVerified == True:
                        login(request, user)
                        return HttpResponse(json.dumps({"msg": "Logged in successfully.", "accountSetup": isAccountSetup}), content_type="application/json")
                    else:
                        email = user.email
                        return HttpResponse(json.dumps({"msg": "OTP sent to "+email}), content_type="application/json")
            except:
                return HttpResponse(json.dumps({"error": "Email or password must be Incorrect."}), content_type="application/json")
        except Exception as error:
            return HttpResponse(json.dumps({"error": error}), content_type="application/json")

        else:
            return HttpResponse(json.dumps({"error": "Email or password must be Incorrect."}), content_type="application/json")
    return HttpResponse(json.dumps({"error": "You were not suppose be here."}), content_type="application/json")


@csrf_exempt
def registerApp(request):
    if request.method == "POST":
        try:

            body = json.loads(request.body)
            email = body['email']
            pass1 = body['password1']
            pass2 = body['password2']

            if not check(email):
                return HttpResponse(json.dumps({"error": "Invalid Email."}), content_type="application/json")
            elif pass1 != pass2:
                return HttpResponse(json.dumps({"error": "Password Does Not Match."}), content_type="application/json")
            else:
                users = User.objects.filter(email=email).all().count()
                if users == 0:
                    newUser = User.objects.create_user(
                        username=email, email=email, password=pass1)

                    newUser.save()
                    otp = str(random.randint(1000, 9999))
                    profileForNewUser = Profile()
                    profileForNewUser.user = User.objects.filter(
                        email=email).first()
                    profileForNewUser.otp = otp
                    profileForNewUser.events = {"data": []}
                    profileForNewUser.notification = {"data": []}
                    profileForNewUser.isAccountSetup = False
                    profileForNewUser.isVolunteer = False
                    profileForNewUser.isOrganiser = False
                    profileForNewUser.isVerified = False
                    profileForNewUser.save()
                    # https://script.google.com/macros/s/AKfycbzW-cQR5jK5dWpfdH7yJ0Rb_gR9dC7YMn0VFnQU9ZCzhCx7wXZgbnTwDcFDsLo6Vn_V/exec?email=barotjaivin244@gmail.com&subject=auto&body=auto&otp=1234
                    r = requests.get('https://script.google.com/macros/s/AKfycbzW-cQR5jK5dWpfdH7yJ0Rb_gR9dC7YMn0VFnQU9ZCzhCx7wXZgbnTwDcFDsLo6Vn_V/exec?email=' +
                                    email + '&subject=Welcome to Xenesis 2023&body=Hi there&otp='+otp)
                    return HttpResponse(json.dumps({"msg": "OTP sent to "+email}), content_type="application/json")
        except Exception as error:
                    return HttpResponse(json.dumps({"error": error}), content_type="application/json")
    else:
            return HttpResponse(json.dumps({"error": "There already exist a account with this email."}), content_type="application/json")
    return HttpResponse(json.dumps({"error": "You were not suppose be here."}), content_type="application/json")


@csrf_exempt
def locationSetterApp(request):
    if request.method == "POST" and request.session['accountSetup'] == True:
        try: 
            body = json.loads(request.body)
            email = body['email']
            location = body['location']
            user = User.objects.filter(email=email).first()
            profile = Profile.objects.filter(user=user).first()
            profile.location = location
            profile.isVerified = True
            profile.isAccountSetup = True
            profile.save()
            request.session['accountSetup'] = False
            return HttpResponse(json.dumps({"msg": "New Location has been saved.", "location": location}), content_type="application/json")
        except Exception as error:
                    return HttpResponse(json.dumps({"error": error}), content_type="application/json")
    return HttpResponse(json.dumps({"error": "You were not suppose be here."}), content_type="application/json")


@csrf_exempt
def accountSetupApp(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            email = body['email']
            name = body['name']
            college = body['college']
            phone = body['phone']
            profilePic = body['profilePic']
            user = User.objects.filter(email=email).first()
            user.first_name = name
            user.save()
            profile = Profile.objects.filter(user=user).first()
            profile.college = college
            profile.phone = phone
            profile.profilePic = profilePic
            profile.save()
            request.session['accountSetup'] = True
            return HttpResponse(json.dumps({"msg": "Account has been setup."}), content_type="application/json")
        except Exception as error:
            return HttpResponse(json.dumps({"error": error}), content_type="application/json")
    return HttpResponse(json.dumps({"error": "You were not suppose be here."}), content_type="application/json")


@csrf_exempt
def resendotpApp(request):
    if request.method == "POST":
        try: 
            body = json.loads(request.body)
            email = body['email']
            if "passwordRecovery" in body.keys():
                otp = str(random.randint(1000, 9999))
                profile = Profile.objects.filter(
                    user=User.objects.filter(email=email).first()).first()
                profile.otp = otp
                profile.save()
                r = requests.get('https://script.google.com/macros/s/AKfycbzW-cQR5jK5dWpfdH7yJ0Rb_gR9dC7YMn0VFnQU9ZCzhCx7wXZgbnTwDcFDsLo6Vn_V/exec?email=' +email + '&subject=Welcome to Xenesis 2023&body=Hi there&otp='+otp)
                request.session['isPasswordRecovery'] = True
                return HttpResponse(json.dumps({"msg": "OTP sent to "+email + " for Password Verification."}), content_type="application/json")
            else:
                otp = str(random.randint(1000, 9999))
                profile = Profile.objects.filter(user=User.objects.filter(email=email).first()).first()
                profile.otp = otp
                profile.save()
                r = requests.get('https://script.google.com/macros/s/AKfycbzW-cQR5jK5dWpfdH7yJ0Rb_gR9dC7YMn0VFnQU9ZCzhCx7wXZgbnTwDcFDsLo6Vn_V/exec?email=' +email + '&subject=Welcome to Xenesis 2023&body=Hi there&otp='+otp)
                return HttpResponse(json.dumps({"msg": "OTP sent to "+email}), content_type="application/json")
        except Exception as error:
                return HttpResponse(json.dumps({"error": error}), content_type="application/json")
    return HttpResponse(json.dumps({"error": "You were not suppose be here."}), content_type="application/json")


@csrf_exempt
def forgotpasswordApp(request):
    if request.method == "POST" and request.session['isPasswordRecovery'] == True:
        try:
            body = json.loads(request.body)
            email = body['email']
            password1 = body['password1']
            password2 = body['password2']
            if password1 == password2:
                user = User.objects.filter(email=email).first()
                user.set_password(password1)
                print(email, password1, password2)
                request.session['isPasswordRecovery'] = False
                return HttpResponse(json.dumps({"msg": "OTP sent to "+email}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({"error": "Passwords doesn't match."}), content_type="application/json")
        except Exception as error:
                    return HttpResponse(json.dumps({"error": error}), content_type="application/json")
    return HttpResponse(json.dumps({"error": "You were not suppose be here."}), content_type="application/json")


@csrf_exempt
def otpvalidationApp(request):
    if request.method == "POST":
        try:      
            body = json.loads(request.body)
            userOtp = body['otp']
            email = body['email']
            user = Profile.objects.filter(
                user=User.objects.filter(email=email).first()).first()
            if userOtp == user.otp:
                profile = Profile.objects.filter(
                    user=User.objects.filter(email=email).first()).first()
                profile.isVerified = True
                profile.save()
                return HttpResponse(json.dumps({"msg": "The user has been verified."}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({"error": "OTP does not match."}), content_type="application/json")
        except Exception as error:
                    return HttpResponse(json.dumps({"error": error}), content_type="application/json")
    return HttpResponse(json.dumps({"error": "You were not suppose be here."}), content_type="application/json")


@csrf_exempt
def accountsetupApp(request):
    return HttpResponse(json.dumps({"error": "You were not suppose be here."}), content_type="application/json")


@csrf_exempt
def homeDataFetcherApp(request):
    data = {"department": [],"event":[],"gallery":[]}

    departmentArr = Department.objects.all()
    for department in departmentArr:
        data["department"].append(department.name)

    images = Gallery.objects.all()
    for image in images:
        data["gallery"].append(image.path)
    
    events = Event.objects.filter(department=Department.objects.filter(name="Computer Engineering").first()).order_by('name').all()
    eventArr = []
    impEvent = []
    for event in events:
        if event.name != "X - Motion Game Mania":
            eventArr.append([event.name, event.price, event.description, event.tagline,event.posterImage, (event.name).replace(" ", "-").replace("---", ":")])
        else:
            impEvent = [[event.name, event.price, event.description, event.tagline, event.posterImage, (event.name).replace(" ", "-").replace("---", ":")]]
    impEvent.extend(eventArr[:10])
    data["event"] = impEvent

    return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def galleryListApp(request):
    images = Gallery.objects.all()
    imageArr = []
    for image in images:
        imageArr.append(image.path)
    return HttpResponse(json.dumps({"data":imageArr}), content_type="application/json")

@csrf_exempt
def eventListApp(request):
    events = Event.objects.all()
    eventArr = []
    impEvent = []
    for event in events:
        if event.name != "X - Motion Game Mania":
            eventArr.append([event.name, event.price, event.description, event.tagline,event.posterImage, (event.name).replace(" ", "-").replace("---", ":")])
        else:
            impEvent = [[event.name, event.price, event.description, event.tagline, event.posterImage, (event.name).replace(" ", "-").replace("---", ":")]]
    impEvent.extend(eventArr[:20])
    departments = Department.objects.all()
    departmentArr = []
    for department in departments:
        departmentArr.append([department.name,department.abbriviation])
    return HttpResponse(json.dumps({"event":impEvent,"department":departmentArr}), content_type="application/json")

@csrf_exempt
def eventsSearchApp(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            query = body['query']
            events = Event.objects.filter(name__contains=query).order_by('name').all()
            eventArr = []
            impEvent = []
            departmentTempArr = []
            for event in events:
                if event.name != "X - Motion Game Mania":
                    eventArr.append([event.name, event.price, event.description, event.tagline,event.posterImage, (event.name).replace(" ", "-").replace("---", ":")])
                    departmentTempArr.append([event.department.name,event.department.abbriviation])
                else:
                    impEvent = [[event.name, event.price, event.description, event.tagline, event.posterImage, (event.name).replace(" ", "-").replace("---", ":")]]
            impEvent.extend(eventArr[:10])

            tempArr = [['Computer Engineering', 'CE']]
            tempArr.extend(departmentTempArr)

            departmentArr = []
            for i in range(len(impEvent)):
                if tempArr[i] not in departmentArr:
                    departmentArr.append(tempArr[i])
            
            data = {
                "event": impEvent,
                "department" : departmentArr
            }
            return HttpResponse(json.dumps(data), content_type="application/json")
        except Exception as error:
            return HttpResponse(json.dumps({"error": error}), content_type="application/json")    
    return HttpResponse(json.dumps({"error": "You were not suppose be here."}), content_type="application/json")

@csrf_exempt
def eventDetailFetcherApp(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            event = body['event']
            event = Event.objects.filter(name=event).first()
            eventArr = []
            eventArr.append(event.name)
            eventArr.append(event.price)
            eventArr.append(event.description)
            eventArr.append(event.posterImage)
            eventArr.append((event.rules).split("•")[1:] if event.rules != None and event.rules != "" else [])
            eventArr.append(event.round1Title)
            eventArr.append((event.round1).split("•")[1:] if event.round1 != None else [])
            eventArr.append(event.round2Title)
            eventArr.append((event.round2).split("•")[1:] if event.round2 != None else [])
            eventArr.append(event.round3Title)
            eventArr.append((event.round3).split("•")[1:] if event.round3 != None else [])
            eventArr.append(event.round4Title)
            eventArr.append((event.round4).split("•")[1:] if event.round4 != None else [])
            eventArr.append(event.round5Title)
            eventArr.append((event.round5).split("•")[1:] if event.round5 != None else [])
            eventArr.append(event.coordinator1.user.first_name)
            eventArr.append(event.coordinator2.user.first_name)
            return HttpResponse(json.dumps({"data":eventArr}), content_type="application/json")
        except Exception as error:
            return HttpResponse(json.dumps({"error": error}), content_type="application/json")
    return HttpResponse(json.dumps({"error": "You were not suppose be here."}), content_type="application/json")

@csrf_exempt
def QRScanner(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            if "uuid" in body.keys():
                uuid = body['uuid']
                ticket = Ticket.objects.filter(qrCodeData=uuid).first()
                if ticket is not None:
                    if ticket.userCount >0:
                        count = 1
                        if ticket.owner1 != None:
                            count=count+1
                        if ticket.owner2 != None:
                            count=count+1
                        if ticket.owner3 != None:
                            count=count+1
                        if ticket.owner4 != None:
                            count=count+1
                        temp = {}
                        temp["id"] = ticket.id
                        temp["profilePic"] = ticket.owner.profilePic
                        temp["username"] = ticket.owner.user.first_name
                        temp["email"] = ticket.owner.user.email
                        if ticket.event.isTeamEvent != True:
                            temp["price"] = ticket.event.price
                        else: 
                            temp["price"] = ticket.event.teamPrice
                        temp["eventName"] = ticket.event.name
                        temp["isPaid"] = ticket.isPaid
                        temp["qrCodeData"] = ticket.qrCodeData
                        temp["isTeamPriceFull"] = ticket.event.isTeamPriceFull
                        try:
                            temp["userCount"] = count
                            if count != 1:
                                temp["total"] = count*int(ticket.event.price)
                        except:
                            temp["userCount"] = 1
                            temp["total"] = 0
                        return HttpResponse(json.dumps({"data":temp}),content_type="application/json")
                    else:
                        return HttpResponse(json.dumps({"error":"Ticket Has already been used."}),content_type="application/json")
                else:
                    return HttpResponse(json.dumps({"error":"Ticket Does Not Exist."}),content_type="application/json")
            elif "ticketId" in body.keys():
                ticketId = body['ticketId']
                ticket = Ticket.objects.filter(id=ticketId).first()
                if ticket.userCount >0:
                    ticket.userCount = ticket.userCount - 1
                    ticket.save()
                    return HttpResponse(json.dumps({"msg":"Ticket Has Been Confirmed."}),content_type="application/json")
                else:
                    return HttpResponse(json.dumps({"error":"Ticket Has already been used."}),content_type="application/json")
            else:
                return HttpResponse(json.dumps({"error":"Server Didnot Recieve QR code. Please Rescan the code."}),content_type="application/json")
        except Exception as error:
            return HttpResponse(json.dumps({"error": error}), content_type="application/json")
    return HttpResponse(json.dumps({"error":"You were not supposed to be here"}),content_type="application/json")
        
