from django.shortcuts import render
from django.http import HttpResponse
from api.models import Profile, Ticket, Event, Ticket, Department
import json
from django.views.decorators.clickjacking import xframe_options_exempt
import random
import folium


def index(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            totalAmount = 0
            totalevent = []
            departmentArr = {}
            eventArr = {}
            tickets = Ticket.objects.all()
            events = Event.objects.all()
            userCount = Profile.objects.all().count()
            eventCount = events.count()
            ticketCount = tickets.count()
            ticketCountNotPaid = tickets.filter(isPaid=False).count()
            totalPaidUsers = 0
            users = []
            for ticket in tickets:
                if ticket.isPaid == True:
                    if ticket.userCount > 1:
                        if ticket.owner not in users:
                            users.append(ticket.owner)
                            totalPaidUsers = totalPaidUsers + 1
                        if ticket.owner1 not in users:
                            users.append(ticket.owner1)
                            totalPaidUsers = totalPaidUsers + 1
                        if ticket.owner2 not in users:
                            users.append(ticket.owner2)
                            totalPaidUsers = totalPaidUsers + 1
                        if ticket.owner3 not in users:
                            users.append(ticket.owner3)
                            totalPaidUsers = totalPaidUsers + 1
                        if ticket.owner4 not in users:
                            users.append(ticket.owner4)
                            totalPaidUsers = totalPaidUsers + 1
                    else:
                        if ticket.owner not in users:
                            users.append(ticket.owner)
                            totalPaidUsers = totalPaidUsers + 1
            for ticket in tickets:
                event = ticket.event
                try:
                    if ticket.isPaid == True:
                        if event.isTeamEvent == True:
                            totalAmount = totalAmount + int((event.teamPrice).split("-")[0])
                        else:
                            totalAmount = totalAmount + int((event.price).split("-")[0])
                except:
                    pass
                if event.department.name not in departmentArr.keys():
                    if ticket.isPaid == True:
                        departmentArr[event.department.name] = [1, 0, 0]
                    else:
                        departmentArr[event.department.name] = [0, 0, 1]
                else:
                    departmentArr[event.department.name] = [departmentArr[event.department.name][0] + 1, departmentArr[event.department.name][1],departmentArr[event.department.name][2]]
                if event.name not in eventArr:
                    if ticket.isPaid == True:
                        try:
                            if event.isTeamEvent == True:
                                eventArr[event.name] = [1, int((event.teamPrice).split("-")[0]),event.name, event.posterImage,0]
                            else:
                                eventArr[event.name] = [1, int((event.price).split("-")[0]),event.name, event.posterImage,0]
                        except:
                            eventArr[event.name] = [1, int(event.price),event.name, event.posterImage,0]
                    else:
                        try:
                            if event.isTeamEvent == True:
                                eventArr[event.name] = [0, int((event.teamPrice).split("-")[0]),event.name, event.posterImage,1]
                            else:
                                eventArr[event.name] = [0, int((event.price).split("-")[0]),event.name, event.posterImage,1]
                        except:
                            eventArr[event.name] = [0, int(event.price),event.name, event.posterImage,1]
                else:
                    if ticket.isPaid == True:
                        eventArr[event.name] = [eventArr[event.name][0] + 1,eventArr[event.name][1],event.name, event.posterImage,eventArr[event.name][4]]
                    else:
                        eventArr[event.name] = [eventArr[event.name][0],eventArr[event.name][1],event.name, event.posterImage,eventArr[event.name][4]+1]

            for event in eventArr.keys():
                eventpercentage = (eventArr[event][0]/ticketCount)*100
                eventArr[event] = [eventArr[event][0], eventArr[event][1]*eventArr[event][0], eventArr[event][2], eventArr[event][3],eventpercentage,eventArr[event][4]]
            eventArrValue = eventArr.values()
            eventArrValue = sorted(eventArrValue,key=lambda x:x[1])[::-1]
            for event in events:
                if event.department.name not in departmentArr.keys():
                    departmentArr[event.department.name] = [0, 1, 0]
                else:
                    departmentArr[event.department.name] = [departmentArr[event.department.name][0], departmentArr[event.department.name][1]+1,departmentArr[event.department.name][2]]
            context = {
                "departmentArr": zip(departmentArr.keys(), departmentArr.values()), 
                "eventArr":  eventArrValue[:10], 
                "totalAmount": totalAmount , 
                "userCount":userCount,
                "eventCount":eventCount,
                "ticketCount":ticketCount,
                "ticketCountNotPaid":ticketCountNotPaid,
                "totalPaidUsers":totalPaidUsers,
                "ticketsPaid": ticketCount-ticketCountNotPaid,
            }
            return render(request, "dashboard.html", context)
        else:
            return render(request, "404.html")
    return render(request, "404.html")


def data(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            departments = Department.objects.all()
            context ={"departmentArr":departments}
            return render(request, "admintable.html", context)
        else:
            return render(request, "404.html")
    return render(request, "404.html")

def events(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            eventArr = {}
            tickets = Ticket.objects.all()
            ticketCount = tickets.count()
            for ticket in tickets:
                event = ticket.event
                if event.posterImage == "-":
                    event.posterImage = ""
                if event.name not in eventArr:
                    if ticket.isPaid == True:
                        try:
                            if event.isTeamEvent == True:
                                eventArr[event.name] = [1, int((event.teamPrice).split("-")[0]),event.name, event.posterImage,0]
                            else:
                                eventArr[event.name] = [1, int((event.price).split("-")[0]),event.name, event.posterImage,0]
                        except:
                            eventArr[event.name] = [1, int(event.price),event.name, event.posterImage,0]
                    else:
                        try:
                            if event.isTeamEvent == True:
                                eventArr[event.name] = [0, int((event.teamPrice).split("-")[0]),event.name, event.posterImage,1]
                            else:
                                eventArr[event.name] = [0, int((event.price).split("-")[0]),event.name, event.posterImage,1]
                        except:
                            eventArr[event.name] = [0, int(event.price),event.name, event.posterImage,1]
                else:
                    if ticket.isPaid == True:
                        eventArr[event.name] = [eventArr[event.name][0] + 1,eventArr[event.name][1],event.name, event.posterImage,eventArr[event.name][4]]
                    else:
                        eventArr[event.name] = [eventArr[event.name][0],eventArr[event.name][1],event.name, event.posterImage,eventArr[event.name][4]+1]

            for event in eventArr.keys():
                eventpercentage = (eventArr[event][0]/ticketCount)*100
                eventArr[event] = [eventArr[event][0], eventArr[event][1]*eventArr[event][0], eventArr[event][2], eventArr[event][3],eventpercentage,eventArr[event][4]]
            eventArrValue = eventArr.values()
            eventArrValue = sorted(eventArrValue,key=lambda x:x[1])[::-1]
            context = {"eventArr":  eventArrValue}
            return render(request, "admin-events-list.html", context)
        else:
            return render(request, "404.html")
    return render(request, "404.html")

def tableData(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            dataType = request.GET.get("type")
            if dataType == "all": 
                users = Ticket.objects.all()
                userArr = []
                for i in users:
                    paid = "No"
                    if i.isPaid == True:
                        paid = "Yes"
                    userArr.append(["T"+str(i.id),i.owner.user.first_name,i.owner.user.username,i.owner.phone,i.event.department.name,i.event.name,paid,i.owner.college])
                return HttpResponse(json.dumps({"users":userArr}),content_type="application/json")
            if dataType == "event": 
                departmentName = request.GET.get("department")
                events = Event.objects.filter(department=Department.objects.filter(name=departmentName).first()).all()
                eventArr = []
                for i in events:
                    eventArr.append(i.name)
                users = Ticket.objects.filter(event__in=events).all()
                userArr = []
                for i in users:
                    paid = "No"
                    if i.isPaid == True:
                        paid = "Yes"
                    userArr.append(["T"+str(i.id),i.owner.user.first_name,i.owner.user.username,i.owner.phone,i.event.department.name,i.event.name,paid,i.owner.college])
                return HttpResponse(json.dumps({"events":eventArr,"users":userArr}),content_type="application/json")
            if dataType == "final":
                eventName = request.GET.get("event")
                users = Ticket.objects.filter(event=Event.objects.filter(name=eventName).first()).all()
                userArr = []
                for i in users:
                    paid = "No"
                    if i.isPaid == True:
                        paid = "Yes"
                    userArr.append(["T"+str(i.id),i.owner.user.first_name,i.owner.user.username,i.owner.phone,i.event.department.name,i.event.name,paid,i.owner.college])
                return HttpResponse(json.dumps({"users":userArr}),content_type="application/json")
            else:
                return HttpResponse(json.dumps({"data":[]}),content_type="application/json")
        else:
            return render(request, "404.html")
    return render(request, "404.html")


def map(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            users = Profile.objects.all()
            my_map = folium.Map(location=(23.2236,72.6468), zoom_start=14)
            ips = []
            for user in users:
                if user.location["ip"] != "":
                    myAddress = (user.location["lat"], user.location["lng"])
                    if myAddress not in ips:
                        ips.append(myAddress)
                    else:
                        randomAdd =  random.uniform(0.0005, 0.005)
                        randomAdd2 =  random.uniform(0.0005, 0.005)
                        myAddress = (user.location["lat"]+randomAdd, user.location["lng"]+randomAdd2)
                    
                    folium.Marker(myAddress,popup=user.user.first_name).add_to(my_map)
            my_map.save('templates/godMode.html')
            return render(request, "map.html")
        else:
            return render(request, "404.html")
    return render(request, "404.html")

@xframe_options_exempt
def godMode(request):
    return render(request, "godMode.html")