from django.http import HttpResponse
from .models import Profile, Department, Event, Ticket, Notifications, Gallery
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import json
import re
import requests
import random
from django.views.decorators.csrf import csrf_exempt


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
                "eventLink" : (event.name).replace(" ", "-").replace("---", ":"),
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
        "departmentArr": departmentArr,
        "isUser" : isUser,
        "isVolunteer" : isVolunteer,
        "userName" : userName,
        "profilePic" : profilePic
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
    eventData = Event.objects.filter(name=event.replace("-", " ").replace(":", " - ")).first()
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
    round1 = (eventData.round1).split("•")[1:] if eventData.round1 != None else []
    round2 = (eventData.round2).split("•")[1:] if eventData.round2 != None else []
    round3 = (eventData.round3).split("•")[1:] if eventData.round3 != None else []
    round4 = (eventData.round4).split("•")[1:] if eventData.round4 != None else []
    round5 = (eventData.round5).split("•")[1:] if eventData.round5 != None else []
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
    context["winner1"] =  eventData.winner1.user.get_full_name() if eventData.winner1 != None  else ""
    context["winner2"] =  eventData.winner2.user.get_full_name() if eventData.winner2 != None  else ""
    context["winner3"] =  eventData.winner3.user.get_full_name() if eventData.winner3 != None  else ""
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
