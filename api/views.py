from django.http import HttpResponse
from .models import Profile, Department, Event, Ticket
import json
import re
import requests
import random
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.db.models import Q
import uuid
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os



def addData(request):
    if request.user.is_superuser:
        data = pd.read_excel("Xenesis Event Registration 2024 (Responses)3.xlsx")
        # covert to array of rows
        data = data.values.tolist()
        for row in data:
            # create new user
            leader = User.objects.filter(username=row[25]).first()
            if  leader != None:
                leaderProfile = Profile.objects.filter(user=leader).first()
            else:
                leader = User.objects.create_user(username=row[25], email=row[25], password="Ldrp@123", first_name=row[24], last_name="")
                leaderProfile = Profile.objects.create(user=leader, profilePic="0007", phone=row[36], otp="", isVolunteer=False, isOrganiser=True, isAccountSetup=False, isCampainVolunteer=False, isVerified=False, college="LDRP-ITR")
                leader.save()
                leaderProfile.save()
            # create new event
            department = Department.objects.filter(name=row[2]).first()
            newEvent = Event()
            if row[27] != None and str(row[27]) != "nan":
                try:
                    tm1 = User.objects.filter(username=row[27]).first()
                    if tm1 != None:
                        tm1Profile = Profile.objects.filter(user=tm1).first()
                    else:
                        tm1 = User.objects.create_user(username=row[27], email=row[27], password="Ldrp@123", first_name=row[26], last_name="")
                        tm1Profile = Profile.objects.create(user=tm1, profilePic="0001", phone=row[37], otp="", isVolunteer=False, isOrganiser=True, isAccountSetup=False, isCampainVolunteer=False, isVerified=False, college="LDRP-ITR")
                        tm1.save()
                        tm1Profile.save()
                    newEvent.organiser1 = tm1Profile
                    print(row[27])
                except:
                    pass
            if row[29] != None and str(row[29]) != "nan":
                try:
                    
                    tm2 = User.objects.filter(username=row[29]).first()
                    if tm2 != None:
                        tm2Profile = Profile.objects.filter(user=tm2).first()
                    else:
                        tm2 = User.objects.create_user(username=row[29], email=row[29], password="Ldrp@123", first_name=row[28], last_name="")
                        tm2Profile = Profile.objects.create(user=tm2, profilePic="0002", phone=row[38], otp="", isVolunteer=False, isOrganiser=True, isAccountSetup=False, isCampainVolunteer=False, isVerified=False, college="LDRP-ITR")
                        tm2.save()
                        tm2Profile.save()
                    newEvent.organiser2 = tm2Profile
                    print(row[29])
                except:
                    pass
            if row[31] != None and str(row[31]) != "nan":
                try:
                    
                    t3 = User.objects.filter(username=row[31]).first()
                    if t3 != None:
                        tm3Profile = Profile.objects.filter(user=t3).first()
                    else:
                        tm3 = User.objects.create_user(username=row[31], email=row[31], password="Ldrp@123", first_name=row[30], last_name="")
                        tm3Profile = Profile.objects.create(user=tm3, profilePic="0003", phone=row[39], otp="", isVolunteer=False, isOrganiser=True, isAccountSetup=False, isCampainVolunteer=False, isVerified=False, college="LDRP-ITR")
                        tm3.save()
                        tm3Profile.save()
                    newEvent.organiser3 = tm3Profile
                    print(row[31])
                except:
                    pass
            if row[33] != None and str(row[33]) != "nan":
                try:
                    
                    t4 = User.objects.filter(username=row[33]).first()
                    if t4 != None:
                        tm4Profile = Profile.objects.filter(user=t4).first()
                    else:
                        tm4 = User.objects.create_user(username=row[33], email=row[33], password="Ldrp@123", first_name=row[32], last_name="")
                        tm4Profile = Profile.objects.create(user=tm4, profilePic="0004", phone=row[40], otp="", isVolunteer=False, isOrganiser=True, isAccountSetup=False, isCampainVolunteer=False, isVerified=False, college="LDRP-ITR")
                        tm4.save()
                        tm4Profile.save()
                    newEvent.organiser4 = tm4Profile
                    print(row[33])
                except:
                    pass
            if row[35] != None and str(row[35]) != "nan":
                try:
                    
                    tm5 = User.objects.filter(username=row[35]).first()
                    if tm5 != None:
                        tm5Profile = Profile.objects.filter(user=tm5).first()
                    else:
                        tm5 = User.objects.create_user(username=row[35], email=row[35], password="Ldrp@123", first_name=row[34], last_name="")
                        tm5Profile = Profile.objects.create(user=tm5, profilePic="0005", phone=row[41], otp="", isVolunteer=False, isOrganiser=True, isAccountSetup=False, isCampainVolunteer=False, isVerified=False, college="LDRP-ITR")
                        tm5.save()
                        tm5Profile.save()
                    newEvent.organiser5 = tm5Profile
                    print(row[35])
                except:
                    pass
            try:
                if str(row[23]) == "nan":
                    images = []
                else:
                    images = row[23].split(", ")
                    images = [image.strip() for image in images]
                    images = ["https://drive.google.com/thumbnail?&id=" + image.split("id=")[-1] + "&sz=w1000" if str(image) != "nan" else "" for image in images]
                    images = [image for image in images if image != ""]
                imagesData = {"data": images}
            except Exception as e:
                print(e)
                imagesData = {"data": []}
            
            
            newEvent.name = row[0]
            newEvent.link = row[0].replace(" ", "-").replace("---", ":").replace("--", ":").replace(":", "-")
            newEvent.tagline = row[1]
            newEvent.department = department
            newEvent.teamName = row[3]
            newEvent.teamLeader = leaderProfile
            newEvent.price = "" if str(row[4]) == "nan" else row[4]
            newEvent.teamPrice = "" if str(row[5]) == "nan" else row[5]
            newEvent.winnerPrice1 = "" if str(row[7]) == "nan" else row[7]
            newEvent.winnerPrice2 = "" if str(row[8]) == "nan" else row[8]
            newEvent.winnerPrice3 = "" if str(row[42]) == "nan" else row[42]
            newEvent.location = "" if str(row[9]) == "nan" else row[9]
            newEvent.date = row[10]
            newEvent.description = "" if str(row[11]) == "nan" else row[11]
            newEvent.rules = "" if str(row[12]) == "nan" else row[12]
            newEvent.round1Title = "" if str(row[13]) == "nan" else row[13]
            newEvent.round1 = "" if str(row[14]) == "nan" else row[14]
            newEvent.round2Title = row[15]
            newEvent.round2 = "" if str(row[16]) == "nan" else row[16]
            newEvent.round3Title = "" if str(row[17]) == "nan" else row[17]
            newEvent.round3 = "" if str(row[18]) == "nan" else row[18]
            newEvent.round4Title = "" if str(row[19]) == "nan" else row[19]
            newEvent.round4 = "" if str(row[20]) == "nan" else row[20]
            newEvent.round5Title = "" if str(row[21]) == "nan" else row[21]
            newEvent.round5 = "" if str(row[22]) == "nan" else row[22]
            newEvent.posterImage = imagesData["data"][0] if len(images) > 0 else ""
            newEvent.teamParticapantCount = row[6] if type(row[6]) == int else int(str(row[6]).split("-")[1])
            newEvent.teamParticapantCountMin = row[6] if type(row[6]) == int else int(str(row[6]).split("-")[0])
            newEvent.isTeamEvent = True if row[6] != 0 else False
            newEvent.isTeamPriceFull = True
            newEvent.isClosed = False
            newEvent.status = 1
            newEvent.images = imagesData
            newEvent.save()
            print(row[0])
        
        return HttpResponse(data, content_type="application/json")
    else:
        return HttpResponse("Nikal Laude, Admin access karega<br/> <br/>░░░░░░░░░░░░░░░▄▄░░░░░░░░░░░<br/>░░░░░░░░░░░░░░█░░█░░░░░░░░░░<br/>░░░░░░░░░░░░░░█░░█░░░░░░░░░░<br/>░░░░░░░░░░░░░░█░░█░░░░░░░░░░<br/>░░░░░░░░░░░░░░█░░█░░░░░░░░░░<br/>██████▄███▄████░░███▄░░░░░░░<br/>▓▓▓▓▓▓█░░░█░░░█░░█░░░███░░░░<br/>▓▓▓▓▓▓█░░░█░░░█░░█░░░█░░█░░░<br/>▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░█░░░<br/>▓▓▓▓▓▓█░░░░░░░░░░░░░░░░█░░░░<br/>▓▓▓▓▓▓█░░░░░░░░░░░░░░██░░░░░<br/>▓▓▓▓▓▓█████░░░░░░░░░██░░░░░<br/>█████▀░░░░▀▀████████░░░░░░")

def events(request):
    departments = Department.objects.all()
    departmentArr = []
    impEvent = []
    for department in departments:
        events = Event.objects.filter(department=department).order_by('-name').all()
        eventArr = []
        tempDepartment = {
            "departmentName" : department.name
        }
        for event in events:
            tempEvent = {
                "eventName" : event.name,
                "eventPrice" : event.price,
                "eventDescription" : event.description,
                "eventTagline" : event.tagline,
                "eventPosterImage" : "" if event.posterImage == "-" else event.posterImage,
                "eventLink" : event.link,
                "isTeamEvent" : event.isTeamEvent,
                "teamPrice" : event.teamPrice,
                "isTeamPriceFull" : event.isTeamPriceFull,
                "winnerPrice1" : event.winnerPrice1 if event.winnerPrice1 != None else 0 ,
                "winnerPrice2" : event.winnerPrice2 if event.winnerPrice2 != None else 0 ,
                "isClosed" : event.isClosed
                
            }
            eventArr.append(tempEvent)
        tempDepartment["events"] = eventArr
        tempDepartment["eventCount"] = len(eventArr)
        departmentArr.append(tempDepartment)
    context = {
        "data": departmentArr
    }
    return HttpResponse(json.dumps(context), content_type="application/json")

def eventsHome(request):
    departments = Department.objects.all()
    departmentList = []
    departmentArr = []
    for department in departments:
        departmentList.append({"name":department.name,"image":department.posterImage})
        events = Event.objects.filter(department=department).order_by('-name').all()
        for event in events:
            tempEvent = {
                "eventName" : event.name,
                "eventPrice" : event.price,
                "eventDescription" : event.description,
                "eventTagline" : event.tagline,
                "eventPosterImage" : "" if event.posterImage == "-" else event.posterImage,
                "eventLink" : event.link,
                "isTeamEvent" : event.isTeamEvent,
                "teamPrice" : event.teamPrice,
                "isTeamPriceFull" : event.isTeamPriceFull,
                "winnerPrice1" : event.winnerPrice1 if event.winnerPrice1 != None else 0 ,
                "winnerPrice2" : event.winnerPrice2 if event.winnerPrice2 != None else 0 ,
                "isClosed" : event.isClosed
            }
            departmentArr.append(tempEvent)
    random.shuffle(departmentArr)
    departmentArr = departmentArr[:20]
    
    context = {
        "data": departmentArr,
        "departments": departmentList
    }
    return HttpResponse(json.dumps(context), content_type="application/json")

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
    eventData = Event.objects.filter(link=event).first()
    context["isTeamEvent"] = eventData.isTeamEvent
    context["name"] = eventData.name
    context["department"] = eventData.department.name
    context["teamName"] = eventData.teamName
    context["teamLeader"] = eventData.teamLeader.user.get_full_name() if eventData.teamLeader != None else ""
    context["teamPhone"] = eventData.teamLeader.phone if eventData.teamLeader != None else ""
    context["price"] = eventData.teamPrice if eventData.isTeamEvent else eventData.price
    context["winnerPrice1"] = eventData.winnerPrice1
    context["winnerPrice2"] = eventData.winnerPrice2
    context["location"] = eventData.location
    context["date"] = str(eventData.date)
    context["description"] = eventData.description
    context["rules"] = (eventData.rules).split("•")[1:] if eventData.rules != None and eventData.rules != "" else ""
    round1Title = eventData.round1Title if eventData.round1Title != None else ""
    round2Title = eventData.round2Title if eventData.round2Title != None else ""
    round3Title = eventData.round3Title if eventData.round3Title != None else ""
    round4Title = eventData.round4Title if eventData.round4Title != None else ""
    round5Title = eventData.round5Title if eventData.round5Title != None else ""
    context["rounds"] = []
    if round1Title != "":
        try:
            round1 = (eventData.round1).split("•")[1:] if "•" in eventData.round1 else [eventData.round1]  if eventData.round1 != None else []
            if str(round1Title) != "nan" and str(round1) != "nan":
                context["rounds"].append({"title": round1Title,"description": round1})
        except:
            pass
    if round2Title != "":
        try:
            round2 = (eventData.round2).split("•")[1:] if "•" in eventData.round2 else [eventData.round2]  if eventData.round2 != None else []
            if str(round2Title) != "nan" and str(round2) != "nan":
                context["rounds"].append({"title": round2Title,"description": round2})
        except:
            pass
    if round3Title != "":
        try:
            round3 = (eventData.round3).split("•")[1:] if "•" in eventData.round3 else [eventData.round3]  if eventData.round3 != None else []
            if str(round3Title) != "nan" and str(round3) != "nan":
                context["rounds"].append({"title": round3Title,"description": round3})
        except:
            pass
    if round4Title != "":
        try:
            round4 = (eventData.round4).split("•")[1:] if "•" in eventData.round4 else [eventData.round4]  if eventData.round4 != None else []
            if str(round4Title) != "nan" and str(round4) != "nan":
                context["rounds"].append({"title": round4Title,"description": round4})
        except:
            pass
    if round5Title != "":
        try:
            round5 = (eventData.round5).split("•")[1:] if "•" in eventData.round5 else [eventData.round5]  if eventData.round5 != None else []
            if str(round5Title) != "nan" and str(round5) != "nan":
                context["rounds"].append({"title": round5Title,"description": round5})
        except:
            pass
    context["tagline"] = eventData.tagline
    context["posterImage"] = eventData.posterImage
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
    context["isClosed"] = eventData.isClosed
    context["status"] = eventData.status
    context["images"] = eventData.images["data"]
    context["isClosed"] = eventData.isClosed
    context["teamParticapantCount"] = eventData.teamParticapantCount
    context["teamParticapantCountMin"] = eventData.teamParticapantCountMin
    request.session['event'] = eventData.name
    return HttpResponse(json.dumps(context), content_type="application/json")

@csrf_exempt
def ticketVerifer(request, ticketQr):
    if request.method == "POST":
        try:
            isOrganiser = Profile.objects.filter(user=request.user).first().isOrganiser
        except:
            isOrganiser = False
        if request.user.is_authenticated and isOrganiser:
            ticket = Ticket.objects.filter(qrCodeData=ticketQr).first()
            if ticket != None:
                if ticket.isScanned == False:
                    if ticket.isPaid == False:
                        context = {
                            "msg" : "Ticket is not paid",
                            "status" : "error"
                        }
                        return HttpResponse(json.dumps(context), content_type="application/json")
                    else:
                        ticket.isScanned = True
                        ticket.save()
                        context = {
                            "msg" : "Ticket is scanned successfully",
                            "status" : "success"
                        }
                        return HttpResponse(json.dumps(context), content_type="application/json")
                else:
                    context = {
                        "msg" : "Ticket is already scanned",
                        "status" : "error"
                    }
                    return HttpResponse(json.dumps(context), content_type="application/json")
            else:
                context = {
                    "msg" : "Ticket is not valid",
                    "status" : "error"
                }
                return HttpResponse(json.dumps(context), content_type="application/json")
        else:
            context = {
                "msg" : "User is not authenticated or not verified",
                "status" : "error"
            }
            return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        context = {
            "msg" : "Invalid request",
            "status" : "error"
        }
        return HttpResponse(json.dumps(context), content_type="application/json")

@csrf_exempt
def ticketPaymentVerifer(request, ticketQr):
    if request.method == "POST":
        try:
            isCampainVolunteer = Profile.objects.filter(user=request.user).first().isCampainVolunteer
        except:
            isCampainVolunteer = False
        if request.user.is_authenticated and isCampainVolunteer:
            ticket = Ticket.objects.filter(qrCodeData=ticketQr).first()
            if ticket != None:
                if ticket.isPaid == False:
                    ticket.isPaid = True
                    ticket.acceptedBy = Profile.objects.filter(user=request.user).first()
                    ticket.save()
                    context = {
                        "msg" : "Ticket is paid successfully",
                        "status" : "success"
                    }
                    return HttpResponse(json.dumps(context), content_type="application/json")
                else:
                    context = {
                        "msg" : "Ticket is already paid",
                        "status" : "error"
                    }
                    return HttpResponse(json.dumps(context), content_type="application/json")
            else:
                context = {
                    "msg" : "Ticket is not valid",
                    "status" : "error"
                }
                return HttpResponse(json.dumps(context), content_type="application/json")
        else:
            context = {
                "msg" : "User is not authenticated or not verified",
                "status" : "error"
            }
            return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        context = {
            "msg" : "Invalid request",
            "status" : "error"
        }
        return HttpResponse(json.dumps(context), content_type="application/json")

@csrf_exempt
def foodCouponVerifer(request, ticketQr):
    if request.method == "POST":
        try:
            isVolunteer = Profile.objects.filter(user=request.user).first().isVolunteer
        except:
            isVolunteer = False
        if request.user.is_authenticated and isVolunteer:
            coupon = Profile.objects.filter(foodCoupon=ticketQr).first()
            if coupon != None:
                if coupon.isScannedCoupon == False:
                    coupon.isScannedCoupon = True
                    coupon.save()
                    context = {
                        "msg" : "Food coupon is given successfully",
                        "status" : "success"
                    }
                    return HttpResponse(json.dumps(context), content_type="application/json")
                else:
                    context = {
                        "msg" : "Food coupon is already used",
                        "status" : "error"
                    }
                    return HttpResponse(json.dumps(context), content_type="application/json")
            else:
                context = {
                    "msg" : "Food coupon is not valid",
                    "status" : "error"
                }
                return HttpResponse(json.dumps(context), content_type="application/json")
        else:
            context = {
                "msg" : "User is not authenticated or not verified",
                "status" : "error"
            }
            return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        context = {
            "msg" : "Invalid request",
            "status" : "error"
        }
        return HttpResponse(json.dumps(context), content_type="application/json")

def ticketData(request,ticketQr):
    ticket = Ticket.objects.filter(qrCodeData=ticketQr).first()
    if ticket != None:
        count = 1
        if ticket.owner1 != None:
            count=count+1
        if ticket.owner2 != None:
            count=count+1
        if ticket.owner3 != None:
            count=count+1
        if ticket.owner4 != None:
            count=count+1
        context = {}
        context["id"] = ticket.id
        context["profilePic"] = ticket.owner.profilePic
        context["username"] = ticket.owner.user.first_name
        context["email"] = ticket.owner.user.email
        if ticket.event.isTeamEvent != True:
            context["price"] = int(ticket.event.price)
        else: 
            if ticket.event.isTeamPriceFull:
                    context["price"] = int(ticket.event.teamPrice)
            else:
                context["price"] = int(ticket.event.teamPrice) * count
        context["eventName"] = ticket.event.name
        context["isPaid"] = ticket.isPaid
        context["qrCodeData"] = ticket.qrCodeData
        context["isTeamEvent"] = ticket.event.isTeamEvent
        context["isScanned"] = ticket.isScanned
        try:
            context["userCount"] = count
            if count != 1:
                context["total"] = count*int(ticket.event.price)
        except:
            context["userCount"] = 1
            context["total"] = 0
        return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        context = {
            "msg" : "Ticket is not valid",
            "status" : "error"
        }
        return HttpResponse(json.dumps(context), content_type="application/json")

def foodCouponData(request,ticketQr):
    coupon = Profile.objects.filter(foodCoupon=ticketQr).first()
    if coupon != None:
        context ={}
        context["id"] = coupon.id
        context["isFoodCoupon"] = True
        context["qrCodeData"] = coupon.foodCoupon
        context["isScanned"] = coupon.isScannedCoupon
        context["profilePic"] = coupon.profilePic
        context["username"] = coupon.user.first_name
        context["email"] = coupon.user.email
        context["status"] = "success"
        return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        context = {
            "msg" : "Food coupon is not valid",
            "status" : "error"
        }
        return HttpResponse(json.dumps(context), content_type="application/json")

def emailSender(subject,reciver,template,otp):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465,context=context) as connection:  
        sender = "xenesis2024@gmail.com"
        password = "lfhe qufb mnfv nldy"
        connection.login(sender, password)
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
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
        connection.sendmail(sender, reciver, msg.as_string())
    pass

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

def userDetail(request):
    if request.user != None:
        try:
            profile = Profile.objects.filter(user=request.user).first()
            userName = request.user.first_name
            isUser = True
            isCampainVolunteer = profile.isCampainVolunteer
            isVolunteer = profile.isVolunteer
            isOrganiser = profile.isOrganiser
            profilePic = profile.profilePic
            email = profile.user.email
            userId = profile.id
            try:
                remote_addr = request.META.get('HTTP_X_FORWARDED_FOR')
                if remote_addr:
                    ip = remote_addr.split(',')[-1].strip()
                else:
                    ip = request.META.get('REMOTE_ADDR')
                url = "http://ip-api.com/json/" + ip
                response = requests.get(url)
                data = response.json()
                profile.location = {"lat":data["lat"], "lng": data["lon"],"ip":ip}
                profile.save()
            except:
                pass
        except:
            userName = "Anonymous"
            isUser = False
            isVolunteer = False
            isCampainVolunteer = False
            isOrganiser = False
            profilePic = "0001"
            email = "anonymous@gmail.com"
            userId = None
    else:
        isUser = False
        isVolunteer = False
        isOrganiser = False
        isCampainVolunteer = False
        userName = "Anonymous"
        profilePic = "0001"
        email = "anonymous@gmail.com"
        userId = None
    context = {
        "isUser" : isUser,
        "isVolunteer" : isVolunteer,
        "isCampainVolunteer" : isCampainVolunteer,
        "isOrganiser" : isOrganiser,
        "userName" : userName,
        "profilePic" : profilePic,
        "email" : email,
        "userId" : userId
    }
    return HttpResponse(json.dumps(context), content_type="application/json")

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
        email = email.lower().strip()
        password = request.POST['password']
        request.session['emailVerification'] = email
        try:
            user = authenticate(username=email, password=password)
            if user is not None:
                profile = Profile.objects.filter(user=user).first()
                isVerified = profile.isVerified
                isAccountSetup = profile.isAccountSetup
                profile.save()
                if isVerified == True:
                    if isAccountSetup == True:
                        login(request, user)
                        try:
                            userName = request.user.first_name
                            isUser = True
                            isVolunteer = profile.isCampainVolunteer
                            profilePic = profile.profilePic
                        except:
                            userName = "Anonymous"
                            isUser = False
                            isVolunteer = False
                            profilePic = "0001"
                        context ={
                            "isUser" : isUser,
                            "isVolunteer" : isVolunteer,
                            "userName" : userName,
                            "profilePic" : profilePic,
                            "msg": "Login Successfull.",
                            "status":"success"
                        }
                        return HttpResponse(json.dumps(context), content_type="application/json")
                    else:
                        context = {
                            'email' : email,
                            'msg' : 'Please Complete Your Account Setup',
                            'redirect' : 'accountsetup',
                            'status': 'error'
                        }
                        return HttpResponse(json.dumps(context), content_type="application/json")
                else:
                    otp = str(random.randint(1000, 9999))
                    profile.otp = otp
                    profile.save()
                    emailSender("OTP validation for Xenesis 2024",email,"./emailTemplates/resendOTPEmail.html",str(otp))
                    context = {
                        'email' : email,
                        'msg' : 'Please Verify Your Email',
                        'redirect' : 'otp',
                        'status': 'error'
                    }
                    return HttpResponse(json.dumps(context), content_type="application/json")
            else:
                context = {
                    'email' : email,
                    'msg' : 'Invalid Credentials',
                    'status': 'error'
                }
                return HttpResponse(json.dumps(context), content_type="application/json")
        except Exception as error:
            context = {
                    'email' : email,
                    'msg' : 'Invalid Credentials',
                    'status':'error'
                }
            
            return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"msg": "Method Not Allowed",'status':'error'}), content_type="application/json",status=405)

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
        email = email.lower().strip()
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if not check(email):
            context = {
                "error" : "Invalid Email.",
                "status":"error"
            }
            return HttpResponse(json.dumps(context), content_type="application/json")
        elif pass1 != pass2:
            context = {
                "error" : "Password Does Not Match.",
                "status":"error"
            }
            return HttpResponse(json.dumps(context), content_type="application/json")
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
                profileForNewUser.isVerified = True
                profileForNewUser.save()
                emailSender("Welcome to Xenesis 2024",email,"./emailTemplates/welcomeEmail.html",str(otp))
                request.session['emailVerification'] = email
                context = {
                        'email' : email,
                        'msg' : 'Please Complete Your Account Setup',
                        'redirect' : 'otp',
                        'status': 'success'
                    }
                return HttpResponse(json.dumps(context), content_type="application/json")
            else:
                context = {
                    "error" : "User Already Exists.",
                    "status":"error"
                }
                return HttpResponse(json.dumps(context), content_type="application/json")
    
    return HttpResponse(json.dumps({"msg": "Method Not Allowed",'status':'error'}), content_type="application/json",status=405)

@csrf_exempt
def otpvalidation(request):
    if request.method == "POST":
        email = request.session['emailVerification']
        isForgotPassword = request.session.get('forgotPassword',False)
        userOtp = request.POST['otp']
        user = Profile.objects.filter(user=User.objects.filter(email=email).first()).first()
        if userOtp == user.otp:
            profile = Profile.objects.filter(user=User.objects.filter(email=email).first()).first()
            profile.isVerified = True
            profile.save()
            context = {
                        'email' : email,
                        'msg' : 'Please Complete Your Account Setup',
                        'status': 'success'
                    }
            if (profile.isAccountSetup == True):
                context['redirect'] = 'login'
            else:
                context['redirect'] = 'accountsetup'
            if isForgotPassword == True:
                context['redirect'] = 'resetpassword'
                del request.session['forgotPassword']
            return HttpResponse(json.dumps(context), content_type="application/json")
        else:
            context = {
                'error' : "Invalid OTP",
                'status':'error'
            }
            return HttpResponse(json.dumps(context), content_type="application/json")
    return HttpResponse(json.dumps({"msg": "Method Not Allowed",'status':'error'}), content_type="application/json",status=405)

@csrf_exempt
def resetPassword(request):
    if request.method == "POST":
        email = request.session['emailVerification']
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 != password2:
            return HttpResponse(json.dumps({"msg": "Password Does Not Match",'status':'error'}), content_type="application/json")
        else:
            user = User.objects.filter(email=email).first()
            user.set_password(password1)
            user.save()
            return HttpResponse(json.dumps({"msg": "Password Reset Successfull."}), content_type="application/json")
    return HttpResponse(json.dumps({"msg": "Method Not Allowed",'status':'error'}), content_type="application/json",status=405)

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
    return HttpResponse(json.dumps({"msg": "Logout Successfull."}), content_type="application/json")

@csrf_exempt
def accountSetUp(request):
    if request.method == "POST":
        try: 
            email = request.session['emailVerification']
            
            name = request.POST['firstname']
            college = request.POST['college']
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

            return HttpResponse(json.dumps({"msg": "Account Setup Successfull.","status":"success"}), content_type="application/json")
        except Exception as error: 
            print(error)
            return HttpResponse(json.dumps({"msg": error,"status":"error"}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"msg": "Method Not Allowed",'status':'error'}), content_type="application/json",status=405)

@csrf_exempt
def resendOtpWeb(request):
    try: 
        email =  request.session['emailVerification']
        otp = str(random.randint(1000, 9999))
        profile = Profile.objects.filter(user=User.objects.filter(email=email).first()).first()
        profile.otp = otp
        profile.save()
        emailSender("OTP validation for Xenesis 2024",email,"./emailTemplates/resendOTPEmail.html",str(otp))
        return HttpResponse(json.dumps({"msg": "OTP sent to "+email,"status":"success"}), content_type="application/json")
    except Exception as error:
            return HttpResponse(json.dumps({"msg": error,"status":"error"}), content_type="application/json")

@csrf_exempt
def forgotPassword(request):
    if request.method == "POST":
        email = request.POST['email']
        email = email.lower().strip()
        user = User.objects.filter(email=email).first()
        if user is not None:
            otp = str(random.randint(1000, 9999))
            profile = Profile.objects.filter(user=user).first()
            profile.otp = otp
            profile.save()
            request.session['emailVerification'] = email
            request.session['forgotPassword'] = True
            emailSender("Reset Password for Xenesis 2024",email,"./emailTemplates/forgotPWDEmail.html",str(otp))
            return HttpResponse(json.dumps({"msg": "An OTP has been sent to "+email+". Please check your email to reset your password.","status":"success","redirect":"otp"}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"msg": "User Not Found","status":"error"}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"msg": "Method Not Allowed",'status':'error'}), content_type="application/json",status=405)

def myTicket(request):
    if request.user != None:
        try:
            profile = Profile.objects.filter(user=request.user).first()
            foodCoupon = profile.foodCoupon
            isScannedCoupon = profile.isScannedCoupon
            userName = request.user.first_name
            isUser = True
        except:
            isUser = False
    if isUser == True:
        tickets = Ticket.objects.filter(Q(owner=profile)|Q(owner1=profile)|Q(owner2=profile)|Q(owner3=profile)|Q(owner4=profile)).all()
        
        dataTemp = []
        if foodCoupon != "":
            temp ={}
            temp["id"] = profile.id
            temp["isFoodCoupon"] = True
            temp["qrCodeData"] = foodCoupon
            temp["isScanned"] = isScannedCoupon
            temp["profilePic"] = profile.profilePic
            temp["username"] = profile.user.first_name
            temp["email"] = profile.user.email
            dataTemp.append(temp)
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
                temp["price"] = int(ticket.event.price)
            else:
                if ticket.event.isTeamPriceFull:
                    temp["price"] = int(ticket.event.teamPrice)
                else:
                    temp["price"] = int(ticket.event.teamPrice) * count
            temp["eventName"] = ticket.event.name
            temp["isPaid"] = ticket.isPaid
            temp["qrCodeData"] = ticket.qrCodeData
            temp["isTeamEvent"] = ticket.event.isTeamEvent
            temp["isScanned"] = ticket.isScanned
            try:
                temp["userCount"] = count
                if count != 1:
                    temp["total"] = count*int(ticket.event.price)
            except:
                temp["userCount"] = 1
                temp["total"] = 0
            temp["isFoodCoupon"] = False
            dataTemp.append(temp)

        context = {
            "data" : dataTemp
        }
        return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"error": "User Not Found"}), content_type="application/json")

def eventConfirmation(request):
    if request.user != None:
        context = {
            "team" : request.session['team'],
            "event" : request.session['event'],
            "status" : "success"
        }
        return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"msg": "User Not Found","status":"error"}), content_type="application/json")

@csrf_exempt
def addTeamMebers(request):
    if request.method == "POST":
        if request.user != None:
            users = request.POST['users']
            emailArr = users.split(",")
            request.session['team'] = []
            try:
                for i in range(len(emailArr)):
                    user = User.objects.filter(email=emailArr[i]).first()
                    profile = Profile.objects.filter(user=user).first()
                    if user is not None:
                        request.session['team'].append({"name":user.first_name, "email":user.email,"phone":profile.phone})
                context = {
                    "msg" : "Team Members Added Successfully.",
                    "status":"success",
                    "redirect":"eventConfirmation"
                }
                return HttpResponse(json.dumps(context), content_type="application/json")
            except:
                context = {
                    "msg" : "Please confirm emails of your team members.",
                    "status":"error"
                }
                return HttpResponse(json.dumps(context), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"msg": "User Not Found","status":"error"}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"msg": "Method Not Allowed","status":"error"}), content_type="application/json",status=405)


@csrf_exempt
def ticketGenerator(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            try:
                eventName = request.session['event']
                event = Event.objects.filter(name=eventName).first()
                isTeam = event.isTeamEvent
                if not isTeam:
                    if event.isClosed == True:
                        return HttpResponse(json.dumps({"msg": "Registration for this event is closed.","status":"error"}), content_type="application/json")
                    else:
                        user = request.user
                        owner = Profile.objects.filter(user=user).first()
                        owner.foodCoupon = uuid.uuid1()
                        owner.isScannedCoupon = False
                        owner.save()
                        qrCodeData = uuid.uuid1()
                        userCount = 1
                        newTicket = Ticket()
                        newTicket.event = event
                        newTicket.owner = owner
                        newTicket.qrCodeData = qrCodeData
                        newTicket.userCount = userCount
                        newTicket.save()
                        return HttpResponse(json.dumps({"msg": "You are successfully registered. Your registration will get confirmed and you will also see the ticket in your account once you make the payment.","status":"success"}), content_type="application/json")
                else:
                    if event.isClosed == True:
                        return HttpResponse(json.dumps({"msg": "Registration for this event is closed.","status":"error"}), content_type="application/json")
                    else:
                        email = request.session['team'][0]['email']
                        user = User.objects.filter(email=email).first()
                        owner = Profile.objects.filter(user=user).first()
                        owner.foodCoupon = uuid.uuid1()
                        owner.isScannedCoupon = False
                        owner.save()
                        qrCodeData = uuid.uuid1()
                        newTicket = Ticket()
                        newTicket.event = event
                        newTicket.owner = owner
                        try:
                            teamMember1= User.objects.filter(email=request.session['team'][1]["email"]).first()
                            teamMember1Profile = Profile.objects.filter(user=teamMember1).first()
                            teamMember1Profile.foodCoupon = uuid.uuid1()
                            teamMember1Profile.isScannedCoupon = False
                            teamMember1Profile.save()
                            newTicket.owner1 = teamMember1Profile 
                        except:
                            newTicket.owner1 = None
                        try:
                            teamMember2= User.objects.filter(email=request.session['team'][2]["email"]).first()
                            teamMember2Profile = Profile.objects.filter(user=teamMember2).first()
                            teamMember2Profile.foodCoupon = uuid.uuid1()
                            teamMember2Profile.isScannedCoupon = False
                            teamMember2Profile.save()
                            newTicket.owner2 = teamMember2Profile 
                        except:
                            newTicket.owner2 = None
                        try:
                            teamMember3= User.objects.filter(email=request.session['team'][3]["email"]).first()
                            teamMember3Profile = Profile.objects.filter(user=teamMember3).first()
                            teamMember3Profile.foodCoupon = uuid.uuid1()
                            teamMember3Profile.isScannedCoupon = False
                            teamMember3Profile.save()
                            newTicket.owner3 = teamMember3Profile 
                        except:
                            newTicket.owner3 = None
                        try:
                            teamMember4= User.objects.filter(email=request.session['team'][4]["email"]).first()
                            teamMember4Profile = Profile.objects.filter(user=teamMember4).first()
                            teamMember4Profile.foodCoupon = uuid.uuid1()
                            teamMember4Profile.isScannedCoupon = False
                            teamMember4Profile.save()
                            newTicket.owner4 = teamMember4Profile 
                        except:
                            newTicket.owner4 = None
                        newTicket.qrCodeData = qrCodeData
                        newTicket.userCount = len(request.session['team'])
                        newTicket.save()
                        request.session['team'] = []
                        return HttpResponse(json.dumps({"msg": "You are successfully registered. Your registration will get confirmed and you will also see the ticket in your account once you make the payment.","status":"success"}), content_type="application/json")
            except Exception as error:
                return HttpResponse(json.dumps({"msg": str(error),"status":"error"}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"msg": "User Not Found","status":"error"}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"msg": "Method Not Allowed","status":"error"}), content_type="application/json",status=405)

@csrf_exempt
def dataOutper(request):
    if user.is_superuser:
        for event in Event.objects.all():
            eventName = event.name
            department = event.department.name
            tickets = Ticket.objects.filter(event=event).all()
            paid = 0
            unpaid = 0
            data = []
            for ticket in tickets:
                if ticket.event.isTeamEvent:
                    if ticket.isPaid:
                        paid += ticket.userCount
                    else:
                        unpaid += ticket.userCount
                else:
                    if ticket.isPaid:
                        paid += 1
                    else:
                        unpaid += 1
            data.append(department+","+eventName+","+str(paid)+","+str(unpaid))
        return HttpResponse(json.dumps({"data":data}), content_type="application/json")

@csrf_exempt
def closeEvents(request):
    if user.is_superuser:
        for event in Event.objects.all():
            event.isClosed = True
            event.save()
        return HttpResponse("Done")

@csrf_exempt
def dbDownload(request):
    if request.user.is_superuser:
        # copy the database file to the static folder
        os.system("cp db.sqlite3 static/")
        return HttpResponse("<a href='/static/db.sqlite3' download>Download</a>")
    
@csrf_exempt
def checkUserEmail(request):
    if request.method == "POST":
        email = request.POST['email']
        user = User.objects.filter(email=email).first()
        if user is not None:
            return HttpResponse(json.dumps({"msg": email + " does exist in our Database.","status":"success"}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"msg": "Email does not exist in our Database","status":"error"}), content_type="application/json")