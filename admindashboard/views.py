from django.shortcuts import render
from django.http import HttpResponse
from api.models import Profile, Ticket, Event, Ticket, Department
import json
# Create your views here.


def index(request):
    totalAmount = 0
    totalevent = []
    departmentArr = {}
    eventArr = {}
    tickets = Ticket.objects.all()
    events = Event.objects.all()
    userCount = Profile.objects.all().count()
    eventCount = events.count()
    ticketCount = tickets.count()
    
    for ticket in tickets:
        event = ticket.event
        totalAmount = totalAmount + int((event.price).split("-")[0])
        if event.department.name not in departmentArr.keys():
            departmentArr[event.department.name] = [1, 0]
        else:
            departmentArr[event.department.name] = [
                departmentArr[event.department.name][0] + 1, 0]
        if event.name not in eventArr:
            eventArr[event.name] = [1, int((event.price).split("-")[0]),event.name, event.posterImage]
        else:
            eventArr[event.name] = [eventArr[event.name][0] + 1,eventArr[event.name][1],event.name, event.posterImage]

    for event in eventArr.keys():
        eventArr[event] = [eventArr[event][0], eventArr[event][1]*eventArr[event][0], eventArr[event][2], eventArr[event][3]]
    eventArrValue = eventArr.values()
    eventArrValue = sorted(eventArrValue,key=lambda x:x[1])[::-1]
    for event in events:
        if event.department.name not in departmentArr.keys():
            departmentArr[event.department.name] = [0, 1]
        else:
            departmentArr[event.department.name] = [departmentArr[event.department.name][0], departmentArr[event.department.name][1]+1]
    context = {"departmentArr": zip(departmentArr.keys(), departmentArr.values()), "eventArr":  eventArrValue[:10], "totalAmount": totalAmount , "userCount":userCount,"eventCount":eventCount,"ticketCount":ticketCount}
    return render(request, "dashboard.html", context)


def data(request):
    departments = Department.objects.all()
    context ={"departmentArr":departments}
    return render(request, "admintable.html", context)

def events(request):
    eventArr = {}
    tickets = Ticket.objects.all()
    
    for ticket in tickets:
        event = ticket.event
        if event.name not in eventArr:
            eventArr[event.name] = [1, int((event.price).split("-")[0]),event.name, event.posterImage]
        else:
            eventArr[event.name] = [eventArr[event.name][0] + 1,eventArr[event.name][1],event.name, event.posterImage]

    for event in eventArr.keys():
        eventArr[event] = [eventArr[event][0], eventArr[event][1]*eventArr[event][0], eventArr[event][2], eventArr[event][3]]
    eventArrValue = eventArr.values()
    eventArrValue = sorted(eventArrValue,key=lambda x:x[1])[::-1]
    context = {"eventArr":  eventArrValue}
    return render(request, "admin-events-list.html", context)

def tableData(request):
    dataType = request.GET.get("type")
    if dataType == "event": 
        departmentName = request.GET.get("department")
        events = Event.objects.filter(department=Department.objects.filter(name=departmentName).first()).all()
        eventArr = []
        for i in events:
            eventArr.append(i.name)
        users = Ticket.objects.filter(event__in=events).all()
        userArr = []
        owner = []
        for i in users:
            if i.owner.user.first_name not in owner:
                owner.append(i.owner.user.first_name)
                userArr.append([i.owner.user.first_name,i.owner.user.username,i.owner.phone,i.owner.college])
        return HttpResponse(json.dumps({"events":eventArr,"users":userArr}),content_type="application/json")
    if dataType == "final":
        eventName = request.GET.get("event")
        users = Ticket.objects.filter(event=Event.objects.filter(name=eventName).first()).all()
        userArr = []
        owner = []
        for i in users:
            if i.owner.user.first_name not in owner:
                owner.append(i.owner.user.first_name)
                userArr.append([i.owner.user.first_name,i.owner.user.username,i.owner.phone,i.owner.college])
        return HttpResponse(json.dumps({"users":userArr}),content_type="application/json")
    else:
        return HttpResponse(json.dumps({"data":[]}),content_type="application/json")

def singin(request):
    return HttpResponse("Admin Login")
