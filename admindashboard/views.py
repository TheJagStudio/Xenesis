from django.shortcuts import render
from django.http import HttpResponse
from api.models import Profile, Ticket, Event, Ticket, Department
import json
from django.views.decorators.clickjacking import xframe_options_exempt
import random
import folium
import uuid


def index(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
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
        if request.user.is_staff:
            departments = Department.objects.all()
            context ={"departmentArr":departments}
            return render(request, "admintable.html", context)
        else:
            return render(request, "404.html")
    return render(request, "404.html")

def events(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            eventArr = {}
            tickets = Ticket.objects.all()
            ticketCount = tickets.count()
            for ticket in tickets:
                event = ticket.event
                userCount = ticket.userCount
                if event.posterImage == "-":
                    event.posterImage = ""
                if event.name not in eventArr:
                    if ticket.isPaid == True:
                        try:
                            if event.isTeamEvent == True:
                                eventArr[event.name] = [1, int((event.teamPrice).split("-")[0]),event.name, event.posterImage,0,userCount]
                            else:
                                eventArr[event.name] = [1, int((event.price).split("-")[0]),event.name, event.posterImage,0,userCount]
                        except:
                            eventArr[event.name] = [1, int(event.price),event.name, event.posterImage,0,userCount]
                    else:
                        try:
                            if event.isTeamEvent == True:
                                eventArr[event.name] = [0, int((event.teamPrice).split("-")[0]),event.name, event.posterImage,1,userCount]
                            else:
                                eventArr[event.name] = [0, int((event.price).split("-")[0]),event.name, event.posterImage,1,userCount]
                        except:
                            eventArr[event.name] = [0, int(event.price)*userCount,event.name, event.posterImage,1,userCount]
                else:
                    if ticket.isPaid == True:
                        eventArr[event.name] = [eventArr[event.name][0] + 1,eventArr[event.name][1],event.name, event.posterImage,eventArr[event.name][4],eventArr[event.name][5]]
                    else:
                        eventArr[event.name] = [eventArr[event.name][0],eventArr[event.name][1],event.name, event.posterImage,eventArr[event.name][4]+1,eventArr[event.name][5]]

            for event in eventArr.keys():
                eventpercentage = (eventArr[event][0]/ticketCount)*100
                totalUser = eventArr[event][0]*eventArr[event][5]
                eventArr[event] = [eventArr[event][0], eventArr[event][1]*eventArr[event][0], eventArr[event][2], eventArr[event][3],eventpercentage,eventArr[event][4],eventArr[event][5],totalUser]
            eventArrValue = eventArr.values()
            eventArrValue = sorted(eventArrValue,key=lambda x:x[1])[::-1]
            context = {"eventArr":  eventArrValue}
            return render(request, "admin-events-list.html", context)
        else:
            return render(request, "404.html")
    return render(request, "404.html")

def tableData(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
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
            if dataType == "allfinal":
                users = Profile.objects.all()
                userArr = []
                count = 0
                for i in users:
                    count = count + 1
                    try:
                        phone = str(int(i.phone))
                    except:
                        phone = ''
                    userArr.append([str(count),i.user.first_name,i.user.username,phone,str(i.isOrganiser),str(i.isVolunteer),str(i.isCampainVolunteer),i.college])
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
        if request.user.is_staff:
            users = Profile.objects.all()
            my_map = folium.Map(location=(23.2236,72.6468), zoom_start=14)
            ips = []
            count = {}
            for user in users:
                isTicketOwner = Ticket.objects.filter(owner=user).first()
                if not isTicketOwner:
                    isTicketOwner = Ticket.objects.filter(owner1=user).first()
                if not isTicketOwner:
                    isTicketOwner = Ticket.objects.filter(owner2=user).first()
                if not isTicketOwner:
                    isTicketOwner = Ticket.objects.filter(owner3=user).first()
                if not isTicketOwner:
                    isTicketOwner = Ticket.objects.filter(owner4=user).first()
                
                if user.location["ip"] != "" and isTicketOwner:
                    myAddress = (user.location["lat"], user.location["lng"])
                    try:
                        count[str(user.location["lat"])+","+ str(user.location["lng"])] = count[str(user.location["lat"])+","+ str(user.location["lng"])] +1
                    except:
                        count[str(user.location["lat"])+","+ str(user.location["lng"])] = 1
                    if myAddress not in ips:
                        ips.append(myAddress)
                    else:
                        randomAdd =  random.uniform(0.005, 0.01)
                        randomAdd2 =  random.uniform(0.005, 0.01)
                        myAddress = (user.location["lat"]+randomAdd, user.location["lng"]+randomAdd2)
                    
                    folium.Marker(myAddress,popup=user.user.first_name).add_to(my_map)
            my_map.save('templates/godMode.html')
            return render(request, "map.html",{"count":json.dumps(count,indent=4)})
        else:
            return render(request, "404.html")
    return render(request, "404.html")

@xframe_options_exempt
def godMode(request):
    return render(request, "godMode.html")

def dataMaker(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            # team wise excel for all paid tickets
            tickets = Ticket.objects.all()
            usersData = []
            for ticket in tickets:
                member = []
                if ticket.isPaid == True:
                    try:
                        if ticket.owner:
                            member.append([ticket.id,ticket.event.name,ticket.event.department.name,ticket.owner.user.username,ticket.owner.user.first_name,ticket.owner.phone,ticket.owner.college])
                    except:
                        pass
                    try:
                        if ticket.owner1:
                            member.append([ticket.id,ticket.event.name,ticket.event.department.name,ticket.owner1.user.username,ticket.owner1.user.first_name,ticket.owner1.phone,ticket.owner1.college])
                    except:
                        pass
                    try:
                        if ticket.owner2:
                            member.append([ticket.id,ticket.event.name,ticket.event.department.name,ticket.owner2.user.username,ticket.owner2.user.first_name,ticket.owner2.phone,ticket.owner2.college])
                    except:
                        pass
                    try:
                        if ticket.owner3:
                            member.append([ticket.id,ticket.event.name,ticket.event.department.name,ticket.owner3.user.username,ticket.owner3.user.first_name,ticket.owner3.phone,ticket.owner3.college])
                    except:
                        pass
                    try:
                        if ticket.owner4:
                            member.append([ticket.id,ticket.event.name,ticket.event.department.name,ticket.owner4.user.username,ticket.owner4.user.first_name,ticket.owner4.phone,ticket.owner4.college])
                    except:
                        pass
                    usersData.extend(member)
            return HttpResponse(json.dumps({"users":usersData}),content_type="application/json")
    
def foodEater(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            tickets = Ticket.objects.all()
            user23 = []
            user24 = []
            data = []
            for ticket in tickets:
                if ticket.isPaid == True:
                    if ticket.event:
                        date = str(ticket.event.date)
                        if "23 Feb 2024" in date:
                            if ticket.owner:
                                tempUUID = uuid.uuid4()
                                ticket.owner.foodCoupon = tempUUID
                                ticket.owner.save()
                                user23.append([ticket.owner.user.first_name,ticket.owner.user.username,ticket.owner.phone,ticket.owner.college])
                            if ticket.owner1:
                                tempUUID = uuid.uuid4()
                                ticket.owner1.foodCoupon = tempUUID
                                ticket.owner1.save()
                                user23.append([ticket.owner1.user.first_name,ticket.owner1.user.username,ticket.owner1.phone,ticket.owner1.college])
                            if ticket.owner2:
                                tempUUID = uuid.uuid4()
                                ticket.owner2.foodCoupon = tempUUID
                                ticket.owner2.save()
                                user23.append([ticket.owner2.user.first_name,ticket.owner2.user.username,ticket.owner2.phone,ticket.owner2.college])
                            if ticket.owner3:
                                tempUUID = uuid.uuid4()
                                ticket.owner3.foodCoupon = tempUUID
                                ticket.owner3.save()
                                user23.append([ticket.owner3.user.first_name,ticket.owner3.user.username,ticket.owner3.phone,ticket.owner3.college])
                            if ticket.owner4:
                                tempUUID = uuid.uuid4()
                                ticket.owner4.foodCoupon = tempUUID
                                ticket.owner4.save()
                                user23.append([ticket.owner4.user.first_name,ticket.owner4.user.username,ticket.owner4.phone,ticket.owner4.college])
                        else:
                            if ticket.owner:
                                tempUUID = uuid.uuid4()
                                ticket.owner.foodCoupon2 = tempUUID
                                ticket.owner.save()
                                user24.append([ticket.owner.user.first_name,ticket.owner.user.username,ticket.owner.phone,ticket.owner.college])
                            if ticket.owner1:
                                tempUUID = uuid.uuid4()
                                ticket.owner1.foodCoupon2 = tempUUID
                                ticket.owner1.save()
                                user24.append([ticket.owner1.user.first_name,ticket.owner1.user.username,ticket.owner1.phone,ticket.owner1.college])
                            if ticket.owner2:
                                tempUUID = uuid.uuid4()
                                ticket.owner2.foodCoupon2 = tempUUID
                                ticket.owner2.save()
                                user24.append([ticket.owner2.user.first_name,ticket.owner2.user.username,ticket.owner2.phone,ticket.owner2.college])
                            if ticket.owner3:
                                tempUUID = uuid.uuid4()
                                ticket.owner3.foodCoupon2 = tempUUID
                                ticket.owner3.save()
                                user24.append([ticket.owner3.user.first_name,ticket.owner3.user.username,ticket.owner3.phone,ticket.owner3.college])
                            if ticket.owner4:
                                tempUUID = uuid.uuid4()
                                ticket.owner4.foodCoupon2 = tempUUID
                                ticket.owner4.save()
                                user24.append([ticket.owner4.user.first_name,ticket.owner4.user.username,ticket.owner4.phone,ticket.owner4.college])
            
            # volunteers
            # volunteers =["mishwajani88@gmail.com","tangaur2507@gmail.com","arshi4299@gmail.com","parvashukla26@gmail.com","gajjarjuhi66@gmail.com","parmarjuhi279@gmail.com","devarshisoni28@gmail.com","ruchitpitaliya2003@gmail.com","harshpatel080503@gmail.com","vishvam028@gmail.com","vaishnavisoni0307@gmail.com","ypatel6353@gmail.com","kirthikasundari4@gmail.com","datardimohsinali@gmail.com","adit28012004@gmail.com","parva_22153@ldrp.ac.in","krutikgami354@gmail.com","aasthapatel6244@gmail.com","abhi_22016@ldrp.ac.in","aditi_22014@ldrp.ac.in","krutika8114@gmail.com","vrushtip19@gmail.com","devinpatel0910@gmail.com","bhattkush2170@gmail.com","hetbhat10@gmail.com","parshavshah0504@gmail.com","shivansh_22043@ldrp.ac.in","krima_22113@ldrp.ac.in","pranjalpatel420@gmail.com","sutharsamarth16@gmail.com","rojivadiyamayank@gmail.com","rudram.jhaveri@gmail.com","harshdhameliya3132004@gmail.com","agaraparam@gmail.com","arthdarji12@gmail.com","vinitsuva97@gmail.com","shreyvyas2210@gmail.com","chandancp8904@gmail.com","khushi0630shah@gmail.com","chiragvadhel29@gmail.com","pandyadivya2103@gmail.com","apurv352000@gmail.com","dhruvprajapati0037@gmail.com","vedanshldrp3005@gmail.com","patelkrish8605@gmail.com","vishalprajapati2870@gmail.com","prajapatikushalmukeshkumar@gmail.com","yakshrawal@gmail.com "]
            # count = 0
            # for volunteer in volunteers:
            #     user = Profile.objects.filter(user__email=volunteer).first()
            #     if user:
            #         if user.foodCoupon == "" or user.foodCoupon2 == "":
            #             count = count + 1
            #         tempUUID = uuid.uuid4()
            #         tempUUID2 = uuid.uuid4()
            #         user.foodCoupon = tempUUID2
            #         user.foodCoupon2 = tempUUID
            #         user.save()
            # print(count)
            return HttpResponse(json.dumps({"user24":user24,"user23":user23}),content_type="application/json")
        else:
            return render(request, "404.html")

def memberPerEvent(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            tickets = Ticket.objects.all()
            events = {}
            for ticket in tickets:
                if ticket.event.name not in events.keys():
                    events[ticket.event.name] = 0
                if ticket.owner:
                    events[ticket.event.name] = events[ticket.event.name] + 1
                if ticket.owner1:
                    events[ticket.event.name] = events[ticket.event.name] + 1
                if ticket.owner2:
                    events[ticket.event.name] = events[ticket.event.name] + 1
                if ticket.owner3:
                    events[ticket.event.name] = events[ticket.event.name] + 1
                if ticket.owner4:
                    events[ticket.event.name] = events[ticket.event.name] + 1
                    
            return HttpResponse(json.dumps({"data":events}),content_type="application/json")
        else:
            return render(request, "404.html")
    
def isOrganiserEater(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            profiles = Profile.objects.all()
            for profile in profiles:
                if profile.isOrganiser == True:
                    tempUUID = uuid.uuid4()
                    tempUUID2 = uuid.uuid4()
                    profile.foodCoupon = tempUUID
                    profile.foodCoupon2 = tempUUID2
                    profile.save()
            return HttpResponse(json.dumps({"data":"done"}),content_type="application/json")