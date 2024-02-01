from django.http import HttpResponse
from .models import Profile, Department, Event, Ticket
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import json
import re
import requests
import random
from django.views.decorators.csrf import csrf_exempt
import pandas as pd

def addData(request):
    if request.user.is_superuser:
        data = pd.read_excel("Xenesis Event Registration 2024 (Responses).xlsx")
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
            if row[27] != None:
                try:
                    print(row[27])
                    tm1 = User.objects.filter(username=row[27]).first()
                    if tm1 != None:
                        tm1Profile = Profile.objects.filter(user=tm1).first()
                    else:
                        tm1 = User.objects.create_user(username=row[27], email=row[27], password="Ldrp@123", first_name=row[26], last_name="")
                        tm1Profile = Profile.objects.create(user=tm1, profilePic="0001", phone=row[37], otp="", isVolunteer=False, isOrganiser=True, isAccountSetup=False, isCampainVolunteer=False, isVerified=False, college="LDRP-ITR")
                        tm1.save()
                        tm1Profile.save()
                    newEvent.organiser1 = tm1Profile
                except:
                    pass
            if row[29] != None:
                try:
                    print(row[29])
                    tm2 = User.objects.filter(username=row[29]).first()
                    if tm2 != None:
                        tm2Profile = Profile.objects.filter(user=tm2).first()
                    else:
                        tm2 = User.objects.create_user(username=row[29], email=row[29], password="Ldrp@123", first_name=row[28], last_name="")
                        tm2Profile = Profile.objects.create(user=tm2, profilePic="0002", phone=row[38], otp="", isVolunteer=False, isOrganiser=True, isAccountSetup=False, isCampainVolunteer=False, isVerified=False, college="LDRP-ITR")
                        tm2.save()
                        tm2Profile.save()
                    newEvent.organiser2 = tm2Profile
                except:
                    pass
            if row[31] != None:
                try:
                    print(row[31])
                    t3 = User.objects.filter(username=row[31]).first()
                    if t3 != None:
                        tm3Profile = Profile.objects.filter(user=t3).first()
                    else:
                        tm3 = User.objects.create_user(username=row[31], email=row[31], password="Ldrp@123", first_name=row[30], last_name="")
                        tm3Profile = Profile.objects.create(user=tm3, profilePic="0003", phone=row[39], otp="", isVolunteer=False, isOrganiser=True, isAccountSetup=False, isCampainVolunteer=False, isVerified=False, college="LDRP-ITR")
                        tm3.save()
                        tm3Profile.save()
                    newEvent.organiser3 = tm3Profile
                except:
                    pass
            if row[33] != None:
                try:
                    print(row[33])
                    t4 = User.objects.filter(username=row[33]).first()
                    if t4 != None:
                        tm4Profile = Profile.objects.filter(user=t4).first()
                    else:
                        tm4 = User.objects.create_user(username=row[33], email=row[33], password="Ldrp@123", first_name=row[32], last_name="")
                        tm4Profile = Profile.objects.create(user=tm4, profilePic="0004", phone=row[40], otp="", isVolunteer=False, isOrganiser=True, isAccountSetup=False, isCampainVolunteer=False, isVerified=False, college="LDRP-ITR")
                        tm4.save()
                        tm4Profile.save()
                    newEvent.organiser4 = tm4Profile
                except:
                    pass
            if row[35] != None:
                try:
                    print(row[35])
                    tm5 = User.objects.filter(username=row[35]).first()
                    if tm5 != None:
                        tm5Profile = Profile.objects.filter(user=tm5).first()
                    else:
                        tm5 = User.objects.create_user(username=row[35], email=row[35], password="Ldrp@123", first_name=row[34], last_name="")
                        tm5Profile = Profile.objects.create(user=tm5, profilePic="0005", phone=row[41], otp="", isVolunteer=False, isOrganiser=True, isAccountSetup=False, isCampainVolunteer=False, isVerified=False, college="LDRP-ITR")
                        tm5.save()
                        tm5Profile.save()
                    newEvent.organiser5 = tm5Profile
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
                "eventPosterImage" : event.posterImage,
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
    departmentArr = []
    for department in departments:
        events = Event.objects.filter(department=department).order_by('-name').all()
        for event in events:
            tempEvent = {
                "eventName" : event.name,
                "eventPrice" : event.price,
                "eventDescription" : event.description,
                "eventTagline" : event.tagline,
                "eventPosterImage" : event.posterImage,
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
    context["price"] = eventData.price
    context["winnerPrice1"] = eventData.winnerPrice1
    context["winnerPrice2"] = eventData.winnerPrice2
    context["location"] = eventData.location
    context["date"] = str(eventData.date)
    context["description"] = eventData.description
    context["rules"] = (eventData.rules).split("•")[1:] if eventData.rules != None and eventData.rules != "" else ""
    round1 = (eventData.round1).split("•")[1:] if "•" in eventData.round1 else eventData.round1  if eventData.round1 != None else []
    round2 = (eventData.round2).split("•")[1:] if "•" in eventData.round2 else eventData.round2  if eventData.round2 != None else []
    round3 = (eventData.round3).split("•")[1:] if "•" in eventData.round3 else eventData.round3  if eventData.round3 != None else []
    round4 = (eventData.round4).split("•")[1:] if "•" in eventData.round4 else eventData.round4  if eventData.round4 != None else []
    round5 = (eventData.round5).split("•")[1:] if "•" in eventData.round5 else eventData.round5  if eventData.round5 != None else []
    round1Title = eventData.round1Title if eventData.round1Title != None else ""
    round2Title = eventData.round2Title if eventData.round2Title != None else ""
    round3Title = eventData.round3Title if eventData.round3Title != None else ""
    round4Title = eventData.round4Title if eventData.round4Title != None else ""
    round5Title = eventData.round5Title if eventData.round5Title != None else ""
    context["rounds"] = []
    if round1Title != "":
        context["rounds"].append({"title": round1Title,"description": round1})
    if round2Title != "":
        context["rounds"].append({"title": round2Title,"description": round2})
    if round3Title != "":
        context["rounds"].append({"title": round3Title,"description": round3})
    if round4Title != "":
        context["rounds"].append({"title": round4Title,"description": round4})
    if round5Title != "":
        context["rounds"].append({"title": round5Title,"description": round5})
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
    context["teamParticapantCount"] = eventData.teamParticapantCount
    context["isClosed"] = eventData.isClosed
    context["status"] = eventData.status
    context["images"] = eventData.images["data"]
    context["isClosed"] = eventData.isClosed
    request.session['event'] = eventData.name
    return HttpResponse(json.dumps(context), content_type="application/json")
