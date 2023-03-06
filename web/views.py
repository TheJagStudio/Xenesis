from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt    
from api.models import Profile, Department, Event, Ticket, Notifications
import re
import requests
import random
import json
import uuid
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
sender = "xenesis@ldrp.ac.in"
password = "Auabs@904"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)
# create a function
def emailSender(reciver,template,otp):
    global server

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Link"
    msg['From'] = sender
    msg['To'] = reciver

    f = open(template, "r", encoding="utf-8")
    html = f.read()
    html = html.replace("%%OTP1%%", otp[0])
    html = html.replace("%%OTP2%%", otp[1])
    html = html.replace("%%OTP3%%", otp[2])
    html = html.replace("%%OTP4%%", otp[3])
    part = MIMEText(html, 'html')
    msg.attach(part)
    server.sendmail(sender, reciver, msg.as_string())

def home(request):
    if request.user != None:
        try:
            profile = Profile.objects.filter(user=request.user).first()
            userName = request.user.first_name
            isUser = True
            isVolunteer = profile.isCampainVolunteer
            profilePic = profile.profilePic
        except:
            userName = "Anonymous"
            isUser = False
            isVolunteer = False
            profilePic = "0001"
    else:
        isUser = False
        isVolunteer = False
        userName = ""
        profilePic = "0001"
    departments = Department.objects.all()
    departmentArr = []
    for department in departments:
        departmentArr.append([department.name, department.posterImage])
    events = Event.objects.filter(department=Department.objects.filter(name="Computer Engineering").first()).all().order_by('-name')
    eventArr = []
    impEvent = []
    for event in events:
        if event.name != "X - Motion Game Mania":
            eventArr.append([event.name, (event.price).strip(), event.description, event.tagline,event.posterImage, (event.name).replace(" ", "-").replace("---", ":"),event.isTeamEvent,event.teamPrice])
        else:
            impEvent = [[event.name, (event.price).strip(), event.description, event.tagline,event.posterImage, (event.name).replace(" ", "-").replace("---", ":"),event.isTeamEvent,event.teamPrice]]
    impEvent.extend(eventArr[:10])
    context = {
        "departmentArr": departmentArr[:10],
        "eventArr": impEvent,
        "isUser" : isUser,
        "isVolunteer" : isVolunteer,
        "userName" : userName,
        "profilePic" : profilePic
    }
    return render(request, "index.html", context)

def events(request):
    if request.user != None:
        try:
            profile = Profile.objects.filter(user=request.user).first()
            userName = request.user.first_name
            isUser = True
            isVolunteer = profile.isCampainVolunteer
            profilePic = profile.profilePic
        except:
            userName = "Anonymous"
            isUser = False
            isVolunteer = False
            profilePic = "0001"
    else:
        isUser = False
        isVolunteer = False
        userName = ""
        profilePic = "0001"
    departments = Department.objects.all()
    departmentArr = []
    impEvent = []
    for department in departments:
        events = Event.objects.filter(department=department).order_by('-name').all()
        eventArr = []
        flag = 0
        for event in events:
            if event.name != "X - Motion Game Mania":
                eventArr.append([event.name, event.price, event.description, event.tagline, event.posterImage, (event.name).replace(" ", "-").replace("---", ":"),event.isTeamEvent,event.teamPrice,event.isTeamPriceFull,event.winnerPrice1,event.winnerPrice2])
            else:
                impEvent = [[event.name, event.price, event.description, event.tagline, event.posterImage, (event.name).replace(" ", "-").replace("---", ":"),event.isTeamEvent,event.teamPrice,event.isTeamPriceFull,event.winnerPrice1,event.winnerPrice2]]
                flag = 1
        if flag == 1:
            impEvent.extend(eventArr)
            departmentArr.append([department.name, impEvent, len(eventArr)])
        else:
            departmentArr.append([department.name, eventArr, len(eventArr)])
    context = {
        "departmentArr": departmentArr,
        "isUser" : isUser,
        "isVolunteer" : isVolunteer,
        "userName" : userName,
        "profilePic" : profilePic
    }
    return render(request, "event.html", context)

def aboutus(request):
    if request.user != None:
        try:
            profile = Profile.objects.filter(user=request.user).first()
            userName = request.user.first_name
            isUser = True
            isVolunteer = profile.isCampainVolunteer
            profilePic = profile.profilePic
        except:
            userName = "Anonymous"
            isUser = False
            isVolunteer = False
            profilePic = "0001"
    else:
        isUser = False
        isVolunteer = False
        userName = ""
        profilePic = "0001"
    context={
        "isUser" : isUser,
        "isVolunteer" : isVolunteer,
        "userName" : userName,
        "profilePic" : profilePic
    }
    return render(request, "about-us.html", context)

@csrf_exempt
def signin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        request.session['emailVarification'] = email
        try:
            username = User.objects.filter(email=email).first().username
            user = authenticate(username=username, password=password)
            if user is not None:
                profile = Profile.objects.filter(user=user).first()
                isVerified = profile.isVerified
                isAccountSetup = profile.isAccountSetup
                
                if isVerified == True:
                    if isAccountSetup == True:
                        login(request, user)
                        return redirect("/")
                    else:
                        context = {'email' : email}
                        return redirect("/accountSetUp",context)
                else:
                    print("ran6")
                    email = user.email
                    context ={
                        "success" : "OTP Has Been Sent To Your Mail"
                    }
                    return render(request, "otp-page.html" , context)
        except:
            context = {
                "error": True
            }
            
            return render(request, "login.html",context)
        else:
            context = {
                "error": True
            }
            return render(request, "login.html",context)
    return render(request, "login.html")

def check(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False

@csrf_exempt
def register(request):
    if request.method == "POST": 
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if not check(email):
            context = {
                "error" : "Invalid Email."
            }
            return render(request, "register.html",context)
            #return HttpResponse(json.dumps({"error": "Invalid Email."}), content_type="application/json")
        elif pass1 != pass2:
            context = {
                "error" : "Password Does Not Match."
            }
            return render(request, "register.html",context)
            #return HttpResponse(json.dumps({"error": "Password Does Not Match."}), content_type="application/json")
        else:
            users = User.objects.filter(email=email).all().count()
            if users == 0:
                newUser = User.objects.create_user(username=email, email=email, password=pass1)
                newUser.save()
                otp = str(random.randint(1000, 9999))
                profileForNewUser = Profile()
                profileForNewUser.user = User.objects.filter(email=email).first()
                profileForNewUser.otp = otp
                profileForNewUser.events = {"data": []}
                profileForNewUser.notification = {"data": []}
                profileForNewUser.isAccountSetup = False
                profileForNewUser.isVolunteer = False
                profileForNewUser.isOrganiser = False
                profileForNewUser.isVerified = False
                profileForNewUser.save()
                emailSender(email,"./emailTemplates/welcomeEmail.html",str(otp))
                request.session['emailVarification'] = email
                return render(request, "otp-page.html",{"email": request.session['emailVarification']})
            else:
                context = {
                    "error" : "User Already Exists."
                }
                return render(request, "register.html",context)
    
    return render(request, "register.html")

def event(request, event):
    if request.user != None:
        try:
            profile = Profile.objects.filter(user=request.user).first()
            userName = request.user.first_name
            email = request.user.email
            isUser = True
            isVolunteer = profile.isCampainVolunteer
            profilePic = profile.profilePic
        except:
            userName = "Anonymous"
            email = ""
            isUser = False
            isVolunteer = False
            profilePic = "0001"
    else:
        isUser = False
        isVolunteer = False
        email = ""
        userName = ""
        profilePic = "0001"
    context = {
        "isUser" : isUser,
        "isVolunteer" : isVolunteer,
        "userName" : userName,
        "profilePic" : profilePic,
        "email" : email
    }
    eventData = Event.objects.filter(name=event.replace("-", " ").replace(":", " - ")).first()
    context["isTeamEvent"] = eventData.isTeamEvent
    context["name"] = eventData.name
    context["department"] = eventData.department
    context["teamName"] = eventData.teamName
    context["teamLeader"] = eventData.teamLeader
    context["price"] = eventData.price
    context["winnerPrice1"] = eventData.winnerPrice1
    context["winnerPrice2"] = eventData.winnerPrice2
    context["location"] = eventData.location
    context["date"] = eventData.date
    context["description"] = eventData.description
    context["rules"] = (eventData.rules).split("•")[1:] if eventData.rules != None and eventData.rules != "" else eventData.rules
    round1 = (eventData.round1).split("•")[1:] if eventData.round1 != None else eventData.round1
    round2 = (eventData.round2).split("•")[1:] if eventData.round2 != None else eventData.round2
    round3 = (eventData.round3).split("•")[1:] if eventData.round3 != None else eventData.round3
    round4 = (eventData.round4).split("•")[1:] if eventData.round4 != None else eventData.round4
    round5 = (eventData.round5).split("•")[1:] if eventData.round5 != None else eventData.round5
    round1Title = eventData.round1Title
    round2Title = eventData.round2Title
    round3Title = eventData.round3Title
    round4Title = eventData.round4Title
    round5Title = eventData.round5Title
    context["rounds"] = [[round1Title, round1, len(round1[0]) if round1 != None and round1 != "-" and round1 != " " else 0, 1], [round2Title, round2, len(round2[0]) if round2 != None and round2 != "-" and round2 != " " else 0, 0], [round3Title, round3, len(round3[0]) if round3 != None and round3 != "-" and round3 != " " else 0, 1], [round4Title, round4, len(round4[0]) if round4 != None and round4 != "-" and round4 != " " else 0, 0], [round5Title, round5, len(round5[0]) if round5 != None and round5 != "-" and round5 != " " else 0, 1]]
    context["tagline"] = eventData.tagline
    context["posterImage"] = eventData.posterImage
    context["winner1"] = eventData.winner1
    context["winner2"] = eventData.winner2
    context["winner3"] = eventData.winner3
    context["organisers"] = eventData.organisers
    context["volunteer"] = eventData.volunteer
    context["organiser1"] = eventData.organiser1.user.get_full_name() if eventData.organiser1 != None else ""
    context["organiser1Phone"] = Profile.objects.filter(user=eventData.organiser1.user).first().phone if eventData.organiser1 != None else ""
    context["organiser2"] = eventData.organiser2.user.get_full_name() if eventData.organiser2 != None else ""
    context["organiser2Phone"] = Profile.objects.filter(user=eventData.organiser2.user).first().phone if eventData.organiser2 != None else ""
    context["organiser3"] = eventData.organiser3.user.get_full_name() if eventData.organiser3 != None else ""
    context["organiser3Phone"] = Profile.objects.filter(user=eventData.organiser3.user).first().phone if eventData.organiser3 != None else ""
    context["organiser4"] = eventData.organiser4.user.get_full_name() if eventData.organiser4 != None else ""
    context["organiser4Phone"] = Profile.objects.filter(user=eventData.organiser4.user).first().phone if eventData.organiser4 != None else ""
    context["organiser5"] = eventData.organiser5.user.get_full_name() if eventData.organiser5 != None else ""
    context["organiser5Phone"] = Profile.objects.filter(user=eventData.organiser5.user).first().phone if eventData.organiser5 != None else ""
    context["isTeamEvent"] = eventData.isTeamEvent
    context["teamParticapantCount"] = eventData.teamParticapantCount
    context["isClosed"] = eventData.isClosed
    context["status"] = eventData.status
    context["images"] = eventData.images["data"]
    request.session['event'] = eventData.name
    return render(request, "event-details.html", context)

def otpvalidationWeb(request):
    if request.method == "POST":
        isresendOtp = request.POST.get('resendotp')
        email = request.session['emailVarification'] 
        print(email)
        userOtp = str(request.POST.get('otp1')) + str(request.POST.get('otp2')) + str(request.POST.get('otp3')) + str(request.POST.get('otp4'))
        print('userotp:- ',userOtp)
        user = Profile.objects.filter(user=User.objects.filter(email=email).first()).first()
        print('User :- ',user)
        if userOtp == user.otp:
            print(user,user.otp)
            profile = Profile.objects.filter(user=User.objects.filter(email=email).first()).first()
            profile.isVerified = True
            profile.save()
            return redirect("/accountSetUp/")
        else:
            context = {'error' : "Invalid OTP"}
            return render(request, "otp-page.html",context)
    #404 page
    return render(request, "404.html")

def pageNotFound(request):
    return render(request,"404.html")

def cart(request):
    if request.user != None:
        try:
            profile = Profile.objects.filter(user=request.user).first()
            userName = request.user.first_name
            isUser = True
            isVolunteer = profile.isCampainVolunteer
            profilePic = profile.profilePic
        except:
            userName = "Anonymous"
            isUser = False
            isVolunteer = False
            profilePic = "0001"
    else:
        isUser = False
        isVolunteer = False
        userName = ""
        profilePic = "0001"
    context={
        "isUser" : isUser,
        "isVolunteer" : isVolunteer,
        "userName" : userName,
        "profilePic" : profilePic
    }
    return render(request,"cart.html",context)

def signOut(request):
    logout(request)
    return redirect('/')

def faqs(request):
    if request.user != None:
        try:
            profile = Profile.objects.filter(user=request.user).first()
            userName = request.user.first_name
            isUser = True
            isVolunteer = profile.isCampainVolunteer
            profilePic = profile.profilePic
        except:
            userName = "Anonymous"
            isUser = False
            isVolunteer = False
            profilePic = "0001"
    else:
        isUser = False
        isVolunteer = False
        userName = ""
        profilePic = "0001"
    context = {
        "isUser" : isUser,
        "isVolunteer" : isVolunteer,
        "userName" : userName,
        "profilePic" : profilePic
    }
    return render(request,"faqs.html",context)

def accountSetUp(request):
    if request.method == "POST":
        try: 
            email = request.session['emailVarification']
            
            name = request.POST['firstname']
            #college = body['college']
            phone = request.POST['mobileNo']
            profilePic = request.POST['profilePic']
            user = User.objects.filter(email=email).first()
            user.first_name = name
            user.save()
            profile = Profile.objects.filter(user=user).first()
            profile.college = "LDRP-ITR"
            profile.phone = phone
            profile.profilePic = profilePic
            profile.isAccountSetup = True
            profile.save()

            request.session['accountSetup'] = True

            return redirect('/login')
        except Exception as error: 
            print(error)
            return render(request, "account-setup.html")
            
            
            #return HttpResponse(json.dumps({"error": error}), content_type="application/json")
    return render(request, "account-setup.html")

    #return render(request, 'account-setup.html')

@csrf_exempt
def resendOtpWeb(request):
    try: 
        email =  request.session['email']
        if "passwordRecovery" in body.keys():
            otp = str(random.randint(1000, 9999))
            profile = Profile.objects.filter(user=User.objects.filter(email=email).first()).first()
            profile.otp = otp
            profile.save()
            emailSender(email,"./emailTemplates/forgotPWDEmail.html",str(otp))
            request.session['isPasswordRecovery'] = True
            return HttpResponse(json.dumps({"msg": "OTP sent to "+email + " for Password Verification."}), content_type="application/json")
        else:
            otp = str(random.randint(1000, 9999))
            profile = Profile.objects.filter(
                user=User.objects.filter(email=email).first()).first()
            profile.otp = otp
            profile.save()
            emailSender(email,"./emailTemplates/resendOTPEmail.html",str(otp))
            return HttpResponse(json.dumps({"msg": "OTP sent to "+email}), content_type="application/json")
    except Exception as error:
            return HttpResponse(json.dumps({"error": error}), content_type="application/json")

@csrf_exempt
def ticketVerifer(request):
    if request.user != None:
        try:
            profile = Profile.objects.filter(user=request.user).first()
            userName = request.user.first_name
            isUser = True
            isVolunteer = profile.isCampainVolunteer
            profilePic = profile.profilePic
        except:
            userName = "Anonymous"
            isUser = False
            isVolunteer = False
            profilePic = "0001"
    else:
        isUser = False
        isVolunteer = False
        userName = ""
        profilePic = "0001"
    if isVolunteer == True:
        if request.method == "POST":
            body = json.loads(request.body)
            id = body['id']
            ticket = Ticket.objects.filter(id=id).first()
            if ticket != None:
                
                ticket.acceptedBy = profile
                ticket.isPaid = True
                
                ticket.save()
                return  HttpResponse(json.dumps({"msg": "Ticket has been Paid."}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({"error": "error"}), content_type="application/json")
        tickets = Ticket.objects.all()
        dataTemp = []
        for ticket in tickets:
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
            temp["isTeamPriceFull"] = ticket.event.isTeamPriceFull
            try:
                temp["userCount"] = count
                if count != 1:
                    temp["total"] = count*int(ticket.event.price)
            except:
                temp["userCount"] = count
                temp["total"] = ticket.event.price
            dataTemp.append(temp)
        data = []
        data2 = []
        for i in dataTemp:
            if i["isPaid"]== False:
                data.append(i)
            else:
                data2.append(i)
        data = data[::-1]
        data.extend(data2)
        context = {
            "data" : data,
            "isUser" : isUser,
            "isVolunteer" : isVolunteer,
            "userName" : userName,
            "profilePic" : profilePic
        }
        return render(request, "ticket.html",context)
    else:
        return render(request, "404.html")

def myTicket(request):
    if request.user != None:
        try:
            profile = Profile.objects.filter(user=request.user).first()
            userName = request.user.first_name
            isUser = True
            isVolunteer = profile.isCampainVolunteer
            profilePic = profile.profilePic
            
        except:
            userName = "Anonymous"
            isUser = False
            isVolunteer = False
            profilePic = "0001"
    else:
        isUser = False
        isVolunteer = False
        userName = ""
        profilePic = "0001"
    if isUser == True:
        tickets = Ticket.objects.filter(Q(owner=profile)|Q(owner1=profile)|Q(owner2=profile)|Q(owner3=profile)|Q(owner4=profile)).all()
        
        dataTemp = []
        for ticket in tickets:
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
            if ticket.userCount >0:
                temp["isScanned"] = False
            else:
                temp["isScanned"] = True
            try:
                temp["userCount"] = count
                if count != 1:
                    temp["total"] = count*int(ticket.event.price)
            except:
                temp["userCount"] = 1
                temp["total"] = 0
            dataTemp.append(temp)
        data = []
        data2 = []
        for i in dataTemp:
            if i["isPaid"]== False:
                data.append(i)
            else:
                data2.append(i)
        data = data[::-1]
        data2 = data2[::-1]
        data.extend(data2)
        context = {
            "data" : data,
            "isUser" : isUser,
            "isVolunteer" : isVolunteer,
            "userName" : userName,
            "profilePic" : profilePic
        }
        return render(request, "myTicket.html",context)
    else:
        return render(request, "404.html")

def eventConfirmation(request):
    if request.user != None:
        try:
            profile = Profile.objects.filter(user=request.user).first()
            userName = request.user.first_name
            isUser = True
            isVolunteer = profile.isCampainVolunteer
            profilePic = profile.profilePic
        except:
            userName = "Anonymous"
            isUser = False
            isVolunteer = False
            profilePic = "0001"
    else:
        isUser = False
        isVolunteer = False
        userName = ""
        profilePic = "0001"
    context = {
        "isUser" : isUser,
        "isVolunteer" : isVolunteer,
        "userName" : userName,
        "profilePic" : profilePic,
        "team" : request.session['team'],
        "event" : request.session['event']
    }
    return render(request, "event-confirmation.html",context)

@csrf_exempt
def addTeamMebers(request):
    if request.user != None:
        try:
            profile = Profile.objects.filter(user=request.user).first()
            userName = request.user.first_name
            isUser = True
            isVolunteer = profile.isCampainVolunteer
            profilePic = profile.profilePic
        except:
            userName = "Anonymous"
            isUser = False
            isVolunteer = False
            profilePic = "0001"
    else:
        isUser = False
        isVolunteer = False
        userName = ""
        profilePic = "0001"
    
    if request.method == "POST":
        isForm = request.POST.get('isForm',False)
        if isForm == False:
            body = json.loads(request.body)
            email = body['email']
            user = User.objects.filter(email=email).first()
            if user is not None:
                return HttpResponse(json.dumps({"msg": email + " does exist in our Database."}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({"error": "Email does not exist in our Database"}), content_type="application/json")
        else:
            users = request.POST.get('user')
            emailArr = users.split(",")
            request.session['team'] = []
            try:
                for i in range(len(emailArr)):
                    user = User.objects.filter(email=emailArr[i]).first()
                    profile = Profile.objects.filter(user=user).first()
                    if user is not None:
                        request.session['team'].append({"name":user.first_name, "email":user.email,"phone":profile.phone})
                return redirect("/eventConfirmation/")
            except:
                context = {
                    'email':request.user,
                    "isUser" : isUser,
                    "isVolunteer" : isVolunteer,
                    "userName" : userName,
                    "profilePic" : profilePic,
                    "event" : request.session['event'],
                    "min":Event.objects.filter(name=request.session['event']).first().teamParticapantCountMin,
                    "max":Event.objects.filter(name=request.session['event']).first().teamParticapantCount,
                    "error" : "Please confirm emails of your team members.",
                }
                return render(request, 'event-registration-form.html',context)
    
    context = {
        'email':request.user,
        "isUser" : isUser,
        "isVolunteer" : isVolunteer,
        "userName" : userName,
        "profilePic" : profilePic,
        "event" : request.session['event'],
        "min":Event.objects.filter(name=request.session['event']).first().teamParticapantCountMin,
        "max":Event.objects.filter(name=request.session['event']).first().teamParticapantCount,
    }
    return render(request, 'event-registration-form.html',context)

@csrf_exempt
def ticketGenrator(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            if 'isTeam' not in body.keys():
                eventName = body['event']
                event = Event.objects.filter(name=eventName).first()
                email = body['email']
                user = User.objects.filter(email=email).first()
                owner = Profile.objects.filter(user=user).first()
                qrCodeData = uuid.uuid1()
                userCount = body['userCount']
                newTicket = Ticket()
                newTicket.event = event
                newTicket.owner = owner
                newTicket.qrCodeData = qrCodeData
                newTicket.userCount = userCount
                newTicket.save()
                return HttpResponse(json.dumps({"msg": "You are successfully registered. Your registration will get confirmed and you will also see the ticket in your account once you make the payment."}), content_type="application/json")
            else:
                eventName = body['event']
                event = Event.objects.filter(name=eventName).first()
                email = request.session['team'][0]['email']
                user = User.objects.filter(email=email).first()
                owner = Profile.objects.filter(user=user).first()
                qrCodeData = uuid.uuid1()
                newTicket = Ticket()
                newTicket.event = event
                newTicket.owner = owner
                try:
                    teamMember1= User.objects.filter(email=request.session['team'][1]["email"]).first()
                    teamMember1Profile = Profile.objects.filter(user=teamMember1).first()
                    newTicket.owner1 = teamMember1Profile 
                except:
                    newTicket.owner1 = None
                try:
                    teamMember2= User.objects.filter(email=request.session['team'][2]["email"]).first()
                    teamMember2Profile = Profile.objects.filter(user=teamMember2).first()
                    newTicket.owner2 = teamMember2Profile 
                except:
                    newTicket.owner2 = None
                try:
                    teamMember3= User.objects.filter(email=request.session['team'][3]["email"]).first()
                    teamMember3Profile = Profile.objects.filter(user=teamMember3).first()
                    newTicket.owner3 = teamMember3Profile 
                except:
                    newTicket.owner3 = None
                try:
                    teamMember4= User.objects.filter(email=request.session['team'][4]["email"]).first()
                    teamMember4Profile = Profile.objects.filter(user=teamMember4).first()
                    newTicket.owner4 = teamMember4Profile 
                except:
                    newTicket.owner4 = None
                newTicket.qrCodeData = qrCodeData
                newTicket.userCount = len(request.session['team'])
                newTicket.save()
                request.session['team'] = []
                return HttpResponse(json.dumps({"msg": "You are successfully registered. Your registration will get confirmed and you will also see the ticket in your account once you make the payment."}), content_type="application/json")
        except Exception as error:
            return HttpResponse(json.dumps({"error": str(error)}), content_type="application/json")
    else:
        return render(request, "404.html")

