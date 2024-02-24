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
import datetime



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
            event = ticket.event
            isOrganiser = False
            user = Profile.objects.filter(user=request.user).first()
            if user==event.teamLeader or user == event.organiser1 or user == event.organiser2 or user == event.organiser3 or user == event.organiser4 or user == event.organiser5:
                isOrganiser = True
            if ticket != None :
                if isOrganiser:
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
                        "msg" : "You can't scan ticket of other event",
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
                if ticket.event.isClosed:
                    return HttpResponse(json.dumps({"msg":"Event is closed","status":"error"}), content_type="application/json")
                else:
                    if ticket.isPaid == False:
                        ticket.isPaid = True
                        ticket.acceptedBy = Profile.objects.filter(user=request.user).first()
                        try:
                            owner = ticket.owner
                            owner.foodCoupon = uuid.uuid1()
                            owner.isScannedCoupon = False
                            owner.save()
                        except:
                            pass
                        try:
                            teamMember1Profile = ticket.owner1
                            teamMember1Profile.foodCoupon = uuid.uuid1()
                            teamMember1Profile.isScannedCoupon = False
                            teamMember1Profile.save()
                        except:
                            pass
                        try:
                            teamMember2Profile = ticket.owner2
                            teamMember2Profile.foodCoupon = uuid.uuid1()
                            teamMember2Profile.save()
                            teamMember2Profile.isScannedCoupon = False
                        except:
                            pass
                        try:
                            teamMember3Profile = ticket.owner3
                            teamMember3Profile.foodCoupon = uuid.uuid1()
                            teamMember3Profile.isScannedCoupon = False
                            teamMember3Profile.save()
                        except:
                            pass
                        try:
                            teamMember4Profile = ticket.owner4
                            teamMember4Profile.foodCoupon = uuid.uuid1()
                            teamMember4Profile.isScannedCoupon = False
                            teamMember4Profile.save()
                        except:
                            pass
                        
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
            # coupon = Profile.objects.filter(foodCoupon=ticketQr).first()
            coupon2 = Profile.objects.filter(foodCoupon2=ticketQr).first()
            # if coupon != None:
            #     # check if date is 23rd feb 2024
            #     if datetime.datetime.now().date() == datetime.date(2024, 2, 23):
            #         if coupon.isScannedCoupon == False:
            #             coupon.isScannedCoupon = True
            #             coupon.save()
            #             context = {
            #                 "msg" : "Food coupon is given successfully",
            #                 "status" : "success"
            #             }
            #             return HttpResponse(json.dumps(context), content_type="application/json")
            #         else:
            #             context = {
            #                 "msg" : "Food coupon is already scanned",
            #                 "status" : "error"
            #             }
            #             return HttpResponse(json.dumps(context), content_type="application/json")
            #     else:
            #         context = {
            #             "msg" : "Food coupon can be only used on 23rd feb 2024",
            #             "status" : "error"
            #         }
            #         return HttpResponse(json.dumps(context), content_type="application/json")
            if coupon2 != None:
                if coupon2.isScannedCoupon2 == False:
                    coupon2.isScannedCoupon2 = True
                    coupon2.save()
                    context = {
                        "msg" : "Food coupon is given successfully",
                        "status" : "success"
                    }
                    return HttpResponse(json.dumps(context), content_type="application/json")
                else:
                    context = {
                        "msg" : "Food coupon is already scanned",
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
            profile.college = college
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
            foodCoupon2 = profile.foodCoupon2
            isScannedCoupon = profile.isScannedCoupon
            isScannedCoupon2 = profile.isScannedCoupon2
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
            temp["eventName"] = "Food Coupon (23 Feb 2024)"
            temp["isFoodCoupon"] = True
            temp["qrCodeData"] = foodCoupon
            temp["isScanned"] = isScannedCoupon
            temp["profilePic"] = profile.profilePic
            temp["username"] = profile.user.first_name
            temp["email"] = profile.user.email
            dataTemp.append(temp)
        if foodCoupon2 != "":
            temp ={}
            temp["id"] = profile.id
            temp["eventName"] = "Food Coupon (24 Feb 2024)"
            temp["isFoodCoupon"] = True
            temp["qrCodeData"] = foodCoupon2
            temp["isScanned"] = isScannedCoupon2
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
                        numEventTickets = Ticket.objects.filter(event=event).all().count()
                        if numEventTickets >= event.ticketCount:
                            event.isClosed = True
                            event.save()
                        return HttpResponse(json.dumps({"msg": "You are successfully registered. Your registration will get confirmed and you will also see the ticket in your account once you make the payment.","status":"success"}), content_type="application/json")
                else:
                    if event.isClosed == True:
                        return HttpResponse(json.dumps({"msg": "Registration for this event is closed.","status":"error"}), content_type="application/json")
                    else:
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
    if request.user.is_superuser:
        for event in Event.objects.all():
            event.isClosed = True
            event.save()
        for ticket in Ticket.objects.all():
            if ticket.isPaid == False:
                ticket.delete()
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
        
def foodGiver(request):
    users = ["aditibhalala0820@gmail.com","1054jaypatel@gmail.com","1274vrajsuthar@gmail.com","12harsh2022@gmail.com","283tishyapatel@gmail.com","5611aasthamakwana@gmail.com","767vashishthdesai@gmail.com","aachalspatel784@gmail.com","aakanksha1615@gmail.com","aasthapatel16244@gmail.com","aasthapatel6244@gmail.com","aastharathod2112@gmail.com","aayushi0708patel@gmail.com","abhi_22016@ldrp.ac.in","acharyamanvay@gmail.com","adit28012004@gmail.com","aditi_22014@ldrp.ac.in","aditipatel1705@gmail.com","aditispatel2020@gmail.com","aditispatel2020@gmail.com ","aeshvi309@gmail.com","aeswapatel@gmail.com","agaraparam@gmail.com","agniveshpatel1910@gmail.com","aishuraj633@gmail.com","aishwaryzaveri@gmail.com","akolatarang@gmail.com","akshparikhak28@gmail.com","alimalek28220@gmail.com","amanafasna3@gmail.com","amanafsana3@gmail.com","anagh0106@gmail.com","anirudh2003sharma@gmail.com","anjalee2710@gmail.com","anshudeloli2006@gmail.com","arinprajapati11@gmail.com","arjunlatiwala@gmail.com","arpitrathod252005@gmail.com","arshi4299@gmail.com","arthdarji12@gmail.com","artisolanki222003@gmail.com","aryanrathod410@gmail.com","asheetirpatel@gmail.com","ashwishah1808@gmail.com","axatpatel9824@gmail.com","ayush4sharmaji@gmail.com","ayushipatel5258@gmail.com","ayushsolanki0607@gmail.com","ayushsolanki78716@gmail.com","bansharipatel6595@gmail.com","bansi0341@gmail.com","bbmathurani@gmail.. co.","belanihetvi@gmail.com","bhadanianeel@gmail.com","bhattkrishna0908@gmail.com","bhattkush2170@gmail.com","bhavsardaksh19@gmail.com","bhavyp536@gmail.com","bhumisonghelani@gmail.com","bp8871051@gmail.com","brijkumbhani162@gmail.com","charitreyas@gmail.com","charmi.padh030206@gmail.com","charvimangukiya@gmail.com","chaudharimayur198@gmail.com","chaudharivaibhu18@gmail.com","chaudharymayur198@gmail.com","chaudharyperin4@gmail.com","chetanmeena0811@gmail.com","chiragvadhel29@gmail.com","chothanihasti15@gmail.com","contact.jay.galaxy@gmail.com","d.p.patel2842005@gmail.com","daivikp40@gmail.com","darmik.y.dhanki@gmail.com","darshangoswami229@gmail.com","darshanpatel15105@gmail.com","datardimohsinali@gmail.com","davehardh18@gmail.com","dbjotaniya7806@gmail.com","dbpanchal24@gmail.com","deepajayasri@gmail.com","devanshgajjar04@gmail.com","devanshimodi3112@gmail.com","devanshipatel497@gmail.com ","devanshipatel7414@gmail.com","devanshraval05@gmail.com","devarshisoni28@gmail.com","devinpatel0910@gmail.com","devjani1454@gmail.com","devkipatel10e4@gmail.com","devp1866@gmail.com","devpatel2189@gmail.com","dewanisolanki123@gmail.com","dhairyakanani0602@gmail.com","dhararuparel16@gmail.com","dharmishthabavaghela06@gmail.com","dharmisthabavaghela06@gmail.com","dharmisthapanda66@ gmail. Com","dharmisthapanda66@gmail.com","dharmpatel4284@gmail.com","dharmshayara@gmail.com","dharmshyara@gmail.com","dhavalshapariya7693@gmail.com","dhawanshah.07@gmail.com","dheerdarji1212@gmail.com","dhrumichaudhari72@gmail.com","dhrumip246@gmail.com ","dhruv13542virtual@gmail.com","dhruvilbavarva@gmail.com","dhruvisomaiya9@gmail.com","dhruvjain20102004@gmail.com","dhruvmakwana0165@gmail.com","dhruvmedatiya2004@gmail.com","dhruvpatel.gnr@gmail.com","dhruvshingod01@gmail.com","dhruvtrivedi357@gmail.com","dhruvvaghela1673@gmail.com","dhvani.s.patel30@gmail.com","dhyanagondaliya24@gmail.com","dhyanikhatrani41@gmail.com","disargi11@gmail.com","dishant.asodiya12@gmail.com","dishapatel3951@gmail.com","dishikamistry@gmail.com","divyabalchandani123@gmail.com","divyanhjain@gmail.com","divyanshgopal474@gmail.com","divyapatel2653@gmail.com","divyarathod2292002@gmail.com","divyasolanki7373@gmail.com","divyeshvadher782@gmail.com","diwandarshil1804@gmail.com","diyatrivedi05@gmail.com","djfresh2314@gmail.com","djpandya1901@gmail.com","dkponkiya2106@gmail.com","dnpatel207@gmail.com","dnpatel207@gmail.com ","drashtimankad1@gmail.com","drashtimankadi@gmail.com","drpatel10122005@gmail.com","druv13542vertual@gmail.com","druvmakavana0165@gmail.com","dvpatel168@gmail.com","dvpatel168@gmail.com ","ektavora0708@gmail.com","fenaj105@gmail.com","frefithgohel90@gmail.com","gajjarjuhi66@gmail.com","garalapreet@gmail.com","gargkritika2017@gmail.com","godhaniprinsi0@gmail.com","gorom627@gmail.com","hadiyalhj66@gmail.com","hani_21352@ldrp.ac.in","hanupatel2216@gmail.com","happygnr04@gmail.com ","happysuva@gmail.com","harahpatel.hrp2002@gmail.com","hardirajpara22@gmail.com","hardpatel956519@gmail.com","harmi.patel3200@gmail.com","harsh.patel081004@gmail.com","harshdhameliya3132004@gmail.com","harshilthakkar163@gmail.com","harshilvaliya40@gmail.com","harshpatel080503@gmail.com","harshpatel71761@gmail.com","harshsonaiya09@gmail.com","hastijk83@gmail.com","hayanpatel9104@gmail.com","hc2643405@gmail.com","heathenova2021@gmail.com","heeratit14@gmail.com","heerpatel0511@gmail.com","heeru2501@gmail.com","heetmistry22903@gmail.com","heetpandya14@gmail.com","heleepatel001@gmail.com","hemladani4331@gmail.com","het_22012@ldrp.ac.in","hetbhat10@gmail.com","hetchauhan66@gmail.com","hetp3286@gmail.com","hetpatel6979@gmail.com","hetvikavathiya006@gmail.com","himalikhant@gmail.com","hingrajiyavishva@gmail.com","hiralahir1104@gmail.com","hirenchaudhary909@gmail.com","Hitpatel5114@gmail.com","honeykhanesa@gmail.com","hp333854@gmail.com","hspatel1092004@gmail.com","hypatel0808@gmail.com","irasama01@gmail.com","isha012savaliya@gmail.com","jadavjuhi2406@gmail.com","jagratpatel99@gmail.com","jainampatel5544@gmail.com","jainilprajapati491@gmail.com","jainu2426@gmail.com","janiisha10@gmail.com","janmajeynathvani@gmail.com","Janvi271203@gmail.com","jay_22220@ldrp.ac.in","jaydeepkhandla11@gmail.com","jayp73922@gmail.com","jder612@gmail.com","jeelbathani11@gmail.com","jeelpopat1010@gmail.com","Jeetpateljp2612@gmail.com","jenishpatel2286@gmail.com","Jensichangani400@gmail.com","jimitramani007@gmail.com","joshividhi802@gmail.com","jumangsinh1016@gmail.com","kabirb1612@gmail.com","kandarp.gajjar.460@gmail.com","kandarpjoshi0809@gmail.com ","kandarpmojidra@gmail.com","kanvipatel46@gmail.com","kanzariyagautam12345@gmail.com","karanpatodi99@gmail.com","kashish.savaliya16@gmail.com","katariyavaishali12@gmail.com","kathanparikh13@gmail.com","kathanpatel2020@gmail.com","kauranidivya@gmail.com","kaushal151131@gmail.com","kausharmansuri17@gmail.com","kavy8955@gmail.com","kavyaptl146612@gmail.com","kavyaraj0205@gmail.com","keshvijarsania198@gmail.com","khodbhayadenisa@gmail.com","khuntdhruv007kdj@gmail.com","khushaliparmar934@gmail.com","khushbunathvani7@gmail.com","khushi0630shah@gmail.com","khushi122004@gmail.com","khushijhala3919@gmail.com","khushijoshi969@gmail.com","khushipatelkalipura@gmail.com","khushisom1105@gmail.com","kirthikasundari4@gmail.com","kishanpatidar2004@gmail.com","knp2040@gmail.com","kp892004@gmail.com","kppatel5077@gmail.com","kreshiviroja487@gmail.com","krima_22113@ldrp.ac.in","krinapokiya2311@gmail.com","krishamangukiya0281@gmail.com","krishamodha2004@gmail.com","krishbathani3225@gmail.com","krishna15906@gmail.com","krishnabhanushali2002@gmail.com","krishnamangukiya0281@gmail.com","Krishnapithiya58@gmail.com","krishpatel2282@gmail.com","krishpatel8403@gmail.com","krishpatelkrp@gmail.com","krupa5103@gmail.com","krupaliahir10@gmail.com","krutijasani5325@gmail.com","krutika8114@gmail.com","krutikgami354@gmail.com","kuldiptalsaniya@gmail.com","kunjp4517@gmail.com","kunjsathavara2003@gmail.com","kunjsherathiya65@gmail.com","kush_22013@ldrp.ac.in","kushal.om30@gmail.com","kushalprajapati3603@gmail.com","lambhajayesh@gmail.com","lightxape@gmail.com","limbchayarutvikrl@gmail.com","luvambadiya@gmail.com","mahekpatel112005@gmail.com","mahekposhiya@gmail.com","mahipatel1422006@gmail.com","mahipatel3202@gmail.com","mahir992535@gmail.com","mahirkalavadia8@gmail.com","maitreypandya02@gamil.com","makgrish104@gmail.com","makwanajanvi54@gmail.com","makwanapriyanka0007@gmail.com","mannp1755@gmail.com","manpatel4906@gmail.com","manthanpatel1422006@gmail.com","manushkapadiya2021@gmail.com","Maulipatel2904@gmail.com","mayurvidhani075@gmail.com","meerasachchade14@gmail.com","meet40167.pm@gmail.com","meetahir0073@gmail.com","Meetmavada023@gmail.com","Meetpavaya@gmail.com","meetpokal04@gmail.com","meetsutariya@gmail.com","meetthakkar1980@gmail.com","megalgohil31@gmail.com","meghatrivedi170@gmail.com","mehaupadhyay95@gmail.com","mihirkothari0702@gmail.com","mihirpatel012005@gmail.com","mitp4771@gmail.com","mitraselly47@gmail.com","mohnishmoledina@gmail.com","mosampatel040@gmail.com","mranand960@gmail.com","mrjsutariya@gmail.com ","muchhadiyaharshida@gmail.com","mykyadav17112003@gmail.com","naazpathan2997@gmail.com","nahush0279@gmail.com","naimishharkhani2004@gmail.com","naiya4151@gmail.com","nami.nanavati2812@gmail.com","namrajagani1234@gmail.com","namratamonu28k@gmail.com","nancyp9210@gmail.com","nanushubham20@gmail.com","nayanvora111@gmail.com","neditprmar@gmail.com","needitparmar@gmail.com","neelmerja@gmail.com","nehakumari961610@gmail.com","nehalbavaghela888@gmail.com","nehanshishanghani261@gmail.com","nidhipatel2102000@gmail.com","nihuchavda3105@gmail.com ","niketmaradiya@gmail.com","nilaykalathiya@gmail.com","niralidave1326@gmail.com","nisargpadia@gmail.com","nisargpatel2704@gmail.com","nisargpatel4803@gmail.com","nishtha3205@gmail.com","nupurdave03@gamil.com","oumgadani2004@gmail.com","ozadev03@gmail.com","palakdudhat9066@gmail.com","palakparmar5102002@gmail.com","palashrajpara15@gmail.com","palladani23@gmail.com","panarapurva156@gmail.com","panchalaayush98@gmail.com","panchalurvish93@gmail.com","pandyadivya2103@gmail.com","panesarashivam@gmail.com","parmar.yogin04@gmail.com","parmarchaitali81@gamail.com","parmarhardik9931@gmail.com","parmarheli2005@gmail.com","parmarishita512@gmail.com","parmarjuhi279@gmail.com","parmarurvi507@gmail.com","parmaryogin04@gmail.com","parshavshah0504@gmail.com","parshvaprajapati2004@gmail.com","parthkapadiya231@gmail.com","parthmetkar123@gmail.com","parthparmar.mba@gmail.com","parthparmar3586@gmail.com","parva_22153@ldrp.ac.in","parva300504@gmail.com","parvashukla26@gmail.com","paryan9094@gmail.com","patelabhisek7654@gmail.com","patelaksh396@gmail.com","patelamit67020@gmail.com","Patelarpit4982@gmail.com","pateldharm075@gmail.com","pateldharmendra7981@gmail.com","pateldharmik2107@gmail.com","pateldivy4005@gmial.com","patelgg106@gmail.com","patelhardi0704@gmail.com","patelhenu2004@gmail.com","Patelkrinalb9999@gmail.com","patelkrish1668@gmail.com","Patelmeet1323@gmail.com","pateln1810@gmail.com","patelprachi2101@gmail.com","patelpreet793@gmail.com","Patelprimal4796@gmail.com","patelsavan498@gmail.com","pateltirthkumar7@gmail.com","patelurvi408@gmail.com","patelurvi408@gmail.com ","patilkhushal54321@gmail.com","patoliyanandita0701@gmail.com","patoliyavrunda8833@gmaiil.com","pavayameet@gmail.com","pavitrajoshi1903@gmail.com","pdpatel1911@gmail.com","pinalvk0110@gmail.com","Pkp20500@gmail.com","pm635923@gmail.com","pmanthan1708@gmail.com","pmeet3692@gmail.com","ppranjal420@gmail.com","Prachi.patel703@gmail.com","praj14320@gmail.com","prajapatikrish132005@gmail.com","prajapatikunj475@gmail.com","prajapatipiyush.2609@gmail.com","prajapativashishtha33@gmail.com","pramb2003@gmail.com","pranjalpatel420@gmail.com","prathampatel1504@gmail.com","prathampatel3424@gmail.com","prathamrpatel2602@gmail.com","Pratikdabhi436@gmail.com","pratikjetani14@gmail.com","preetpatel10114@gmail.com","preksham326@gmail.com","preya0712@gmail.com","princegoswami342000@gmail.com","princekukadiya95@gmail.com","princepatel30p5@gmail.com","princypatel2022@gmail.com","prinshu.patel2004@gmail.com","printibamaniya@gmail.com","priyaaa2319@gmail.com","priyanksatani1234@gmail.com","priyanshee.patil@gmail.com","priyanshi9112004@gmail.com","priyanshipatel3612@gmail.com","priyanshisojitra1712@gmail.com","priyanshupatel832@gmail.com","priyavora69@gmail.com","psns4040@gmail.com","purohitbansi09@gmail.com","pushyashah15@gmail.com","rahipatel191@gmail.com","raiyaniharsh5@gmail.com","rajd99504@gmail.com","rajmovaliya08@gmail.com","rajvirupapara1510@gmail.com","rathodsumit1612005@gmail.com","ravaljanvi@gmail.com","ravalkruti301@gmail.com","ravisenjaliya99@gmail.com","rg4631141@gmail.com","ridhampatel2k4@gmail.com","ridhamrathod1205@gmail.com","ridhamshah625@gmail.com","ritikshakotadiya@gmail.com","riyapatel47677@gmail.com","rojivadiyamayank@gmail.com","ronakgodhani027@gmail.com","ronakpatel0347@gmail.com","roshanisolanki11105@gmail.com","rp4766827@gmail.com","ruchitpitaliya2003@gmail.com","rudhram.jhavari@gmail.com","rudra15406@gmail.com","rudram.jhaveri@gmail.com","rupareliyameet7@gmail.com","rushilpatel2903@gmail.com","rutapatolia2005@gmail.com","rutva1043@gmail.com","rutvip488@gmail.com","sahilsenjaliya1809@gmail.com","sandipmistry08@gmail.com","sanjayedu2004@gmail.com","sanjivmudaliar2311@gmail.com","sankhla.smit@gmail.com","sanvichaudhary311@gmail.com","savaliyatrusha41@gmail.com","sejalvaghela755@gmail.com","sentavishantj@gmail.com","sgbapodara@gmail.com","shahshreysds@gmail.com","Shaileshvaniya2586@gmail.com","shekhnoornoor036@gmail.com","shivampatel635272@gmail.com","shivansh_22043@ldrp.ac.in","shraddhabasolanki67@gmail.com","shreyansh17122004@gmail.com","shreyapatidar1977@gmail.com","shreyvyas2210@gmail.com","shubh13052004@gmail.com","shubhamparikh07@gmail.com","shubhpatel918@gmail.com","shubhvikani13@gmail.com","shyamkaneriya2006@gmail.com","shyamvanjani6633@gmail.com","sikha.singh09jan@gmail.com","sinhaujjwal175@gmail.com","smitjoshi224@gmail.com","smsuthar2520@gmail.com","snehachatwani36@gmail.com","snehajadeja24@gmail.com","sojitradarshitpiyushbhai@gmail.com","sojitrahimani174@gmail.com","solankimihir1210@gmail.com","solankisureshkumar25@gmail.com","sonalyadav04g@gmail.com","sorathiyasahil5656@gmail.com","soumyaditya611@gmail.com","sp4078164@gmail.com","srushti2353@gmail.com","Suchi3010patel@gmail.com","sugampatel410313@gmail.com","Suhaniprajapati3105@gmail.com","sutharharshp04@gmail.com","sutharsamarth16@gmail.com","suva.neeja@gmail.com","suva.neeja11@gmail.com","swaminarayanvatsal@gmail.com","swapanil0704@gmail.com","swetasharma1902@gmail.com","t37sharmakrishnac@gmail.com","tanishqmaheshwari225@gmail.com","taniyaambwani26@gmail.com","thakkarkrutika4@gmail.com","thekrishpatel20@gmail.com","thisisrudrab@gmail.com","tilakpatel2424@gmail.com","tirkardhruv67@gmail.com","tirthacharya97@gmail.com","tirthbhinagradiya1604@gmail.com","tirthchomal@gmail.com","tirthpatel162005@gmail.com","tithu244@gmail.com","tusdrj@gmail.com","udaychanpa101@gmail.com","udaychanpa635@gmail.com","udayvasoya603@gmail.com","upadhyaykinjal050@gmail.com","upadhyayraj918@gmail.com","urjasoni0124@gmail.com","urvii1521@gmail.com","urvish7904@gmail.com","vadaliyatirth@gmail.com","vaghasiyapinal2003@gmail.com","vaghelaastha92@gmail.com","vaghelakrushnadevsinh523@gmail.com","vaghelavijay8347@gmail.com","vaibhavsukhwal1345@gmail.com","vaishnavisoni0307@gmail.com","vanpariyapalak@gmail.com","vanshilrathod9904@gmail.com","varcha108@gmail.com","varshilparejiya2004@gmail.com","Vashishthapatel0@gmail.com","vasukpatel025@gmail.com","vasurupapara5@gmail.com","vasuvachhani2004@gmail.com","vedanshldrp3005@gmail.com","vedanthirani99@gmail.com","vedantjoshi2115@gmail.com","vedantshah2401@gmail.com","Vibhathakkar27@gmail.com","vikashbaraiya6512@gmail.com","vinitsuva97@gmail.com","viratdharaiya2004@gmail.com","vishvam028@gmail.com","vishvamaradia25072@gmail.com","vishvldrp7@gmail.com","vishwangsuthar.997@gmail.com","vishwasoni11@gmail.com","vishwasonil@gmail.com","vraj_21244@ldrp.ac.in","vrajc494@gmail.com","vrajp1016@gmail.com","vrajshrimali2410@gmail.com","vrund4591@gmail.com","vrushtip19@gmail.com","vrutikap348@gmail.com","vrutvip1330@gmail.com","vyasanjali17@gmail.com","vyascv5714@gmail.com","yagnikjasoliya@gmail.com","yash10876@gmail.com","yashgajjar2222@gmail.com","yashuvithalani21@gmail.com","yp1102003@gmail.com","ypatel6353@gmail.com","yug p9244@gmail.com","yug190705@gmail.com","zadafiyaraj395@gmail.com","zalak552005@gmail.com","zeelkanudawala@gmail.com","zeelsimejiyal6@gmail.com","zenishadevani@gmail.com","ziyanmansuri2112@gmail.com",]
    data = []
    for user in users:
        try:
            user = User.objects.get(username=user)
            profile = Profile.objects.get(user=user)
            if profile.foodCoupon == "":
                uuidTemp = str(uuid.uuid4())
                profile.foodCoupon = uuidTemp
                data.append([profile.user.first_name,profile.user.email,profile.phone])
                profile.save()
        except:
            pass
    return HttpResponse(json.dumps({"data": data,"status":"success"}), content_type="application/json",status=200)


def allEventTickets(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            user = Profile.objects.filter(user=request.user).first()
            if user.isOrganiser:
                event = Event.objects.filter(Q(teamLeader=user) |Q(organiser1=user) |Q(organiser2=user) |Q(organiser3=user) |Q(organiser4=user) |Q(organiser5=user)).first()
                data = []
                tickets = Ticket.objects.filter(event=event).all()
                for ticket in tickets:
                    temp = []
                    temp.append(ticket.id)
                    temp.append(ticket.owner.user.first_name)
                    temp.append(ticket.owner.user.email)
                    temp.append(ticket.owner.phone)
                    temp.append(ticket.userCount)
                    temp.append(str(ticket.isPaid) )
                    temp.append(str(ticket.isScanned))
                    data.append(temp)
                return HttpResponse(json.dumps({"data": data,"status":"success"}), content_type="application/json",status=200)
        else:
            return HttpResponse(json.dumps({"msg": "User Not Found","status":"error"}), content_type="application/json",status=404)