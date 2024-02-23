from django.shortcuts import render
from django.http import HttpResponse
from api.models import Profile, Ticket, Event, Ticket, Department
from django.contrib.auth.models import User
import json
from django.views.decorators.clickjacking import xframe_options_exempt
import random
import folium
import uuid
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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
            # tickets = Ticket.objects.all()
            # user23 = []
            # user24 = []
            # data = []
            # for ticket in tickets:
            #     if ticket.isPaid == True:
            #         if ticket.event:
            #             date = str(ticket.event.date)
            #             if "23 Feb 2024" in date:
            #                 if ticket.owner:
            #                     tempUUID = uuid.uuid4()
            #                     ticket.owner.foodCoupon = tempUUID
            #                     ticket.owner.save()
            #                     user23.append([ticket.owner.user.first_name,ticket.owner.user.username,ticket.owner.phone,ticket.owner.college])
            #                 if ticket.owner1:
            #                     tempUUID = uuid.uuid4()
            #                     ticket.owner1.foodCoupon = tempUUID
            #                     ticket.owner1.save()
            #                     user23.append([ticket.owner1.user.first_name,ticket.owner1.user.username,ticket.owner1.phone,ticket.owner1.college])
            #                 if ticket.owner2:
            #                     tempUUID = uuid.uuid4()
            #                     ticket.owner2.foodCoupon = tempUUID
            #                     ticket.owner2.save()
            #                     user23.append([ticket.owner2.user.first_name,ticket.owner2.user.username,ticket.owner2.phone,ticket.owner2.college])
            #                 if ticket.owner3:
            #                     tempUUID = uuid.uuid4()
            #                     ticket.owner3.foodCoupon = tempUUID
            #                     ticket.owner3.save()
            #                     user23.append([ticket.owner3.user.first_name,ticket.owner3.user.username,ticket.owner3.phone,ticket.owner3.college])
            #                 if ticket.owner4:
            #                     tempUUID = uuid.uuid4()
            #                     ticket.owner4.foodCoupon = tempUUID
            #                     ticket.owner4.save()
            #                     user23.append([ticket.owner4.user.first_name,ticket.owner4.user.username,ticket.owner4.phone,ticket.owner4.college])
            #             else:
            #                 if ticket.owner:
            #                     tempUUID = uuid.uuid4()
            #                     ticket.owner.foodCoupon2 = tempUUID
            #                     ticket.owner.save()
            #                     user24.append([ticket.owner.user.first_name,ticket.owner.user.username,ticket.owner.phone,ticket.owner.college])
            #                 if ticket.owner1:
            #                     tempUUID = uuid.uuid4()
            #                     ticket.owner1.foodCoupon2 = tempUUID
            #                     ticket.owner1.save()
            #                     user24.append([ticket.owner1.user.first_name,ticket.owner1.user.username,ticket.owner1.phone,ticket.owner1.college])
            #                 if ticket.owner2:
            #                     tempUUID = uuid.uuid4()
            #                     ticket.owner2.foodCoupon2 = tempUUID
            #                     ticket.owner2.save()
            #                     user24.append([ticket.owner2.user.first_name,ticket.owner2.user.username,ticket.owner2.phone,ticket.owner2.college])
            #                 if ticket.owner3:
            #                     tempUUID = uuid.uuid4()
            #                     ticket.owner3.foodCoupon2 = tempUUID
            #                     ticket.owner3.save()
            #                     user24.append([ticket.owner3.user.first_name,ticket.owner3.user.username,ticket.owner3.phone,ticket.owner3.college])
            #                 if ticket.owner4:
            #                     tempUUID = uuid.uuid4()
            #                     ticket.owner4.foodCoupon2 = tempUUID
            #                     ticket.owner4.save()
            #                     user24.append([ticket.owner4.user.first_name,ticket.owner4.user.username,ticket.owner4.phone,ticket.owner4.college])
            
            # volunteers
            volunteers =["mishwajani88@gmail.com","tangaur2507@gmail.com","arshi4299@gmail.com","parvashukla26@gmail.com","gajjarjuhi66@gmail.com","parmarjuhi279@gmail.com","devarshisoni28@gmail.com","ruchitpitaliya2003@gmail.com","harshpatel080503@gmail.com","vishvam028@gmail.com","vaishnavisoni0307@gmail.com","ypatel6353@gmail.com","kirthikasundari4@gmail.com","datardimohsinali@gmail.com","adit28012004@gmail.com","parva_22153@ldrp.ac.in","krutikgami354@gmail.com","aasthapatel6244@gmail.com","abhi_22016@ldrp.ac.in","aditi_22014@ldrp.ac.in","krutika8114@gmail.com","vrushtip19@gmail.com","devinpatel0910@gmail.com","bhattkush2170@gmail.com","hetbhat10@gmail.com","parshavshah0504@gmail.com","shivansh_22043@ldrp.ac.in","krima_22113@ldrp.ac.in","pranjalpatel420@gmail.com","sutharsamarth16@gmail.com","rojivadiyamayank@gmail.com","rudram.jhaveri@gmail.com","harshdhameliya3132004@gmail.com","agaraparam@gmail.com","arthdarji12@gmail.com","vinitsuva97@gmail.com","shreyvyas2210@gmail.com","chandancp8904@gmail.com","khushi0630shah@gmail.com","chiragvadhel29@gmail.com","pandyadivya2103@gmail.com","apurv352000@gmail.com","dhruvprajapati0037@gmail.com","vedanshldrp3005@gmail.com","patelkrish8605@gmail.com","vishalprajapati2870@gmail.com","prajapatikushalmukeshkumar@gmail.com","yakshrawal@gmail.com "]
            count = 0
            for volunteer in volunteers:
                user = Profile.objects.filter(user__email=volunteer).first()
                if user:
                    if user.foodCoupon == "" or user.foodCoupon2 == "":
                        count = count + 1
                    # tempUUID = uuid.uuid4()
                    # tempUUID2 = uuid.uuid4()
                    # user.foodCoupon = tempUUID2
                    # user.foodCoupon2 = tempUUID
                    user.isVolunteer = True
                    user.save()
            print(count)
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
    
def aluminiMaker(request):
    if request.user.is_authenticated and request.user.is_superuser:
        users = [["Ajay Shukla","ajayshukla9662@gmail.com"],["Kishan Jogiya","kishanjogiya11@gmail.com"],["Nihar Makwana","niharmakwana46@gmail.com"],["Nikunj Panelia","nikunjpanelia1192@gmail.com"],["Malek Nadeem Ahemad ","nadeemahamed22699@gmail.com"],["Ronak Hareshkumar Desai","ronakdesai92@gmail.com"],["Dr. Ankit D. Oza","ankit.oza30956@paruluniversity.ac.in"],["Harshid Keraliya","harshidkeraliya@gmail.com"],["Jadav Akashkumar Nitinkumar","jadavakashkumar@gmail.com"],["Ashish Makhija","makhija726@gmail.com"],["Sakshi Thekdi ","sakshithekdi@gmail.com"],["Aniket Purohit","aniket9124@gmail.com"],["Mrugesh Patel","patelmrugesh.2892@gmail.com"],["Darshan Bhavsar","darshanbhavsar4.db@gmail.com"],["Arjun Parmar","abarjunofficial@gmail.com"],["Uchit Viramgama","uchitpatel7@gmail.com"],["Sahil Jain","jainsahil624@gmail.com"],["Ashok Mali","ashokmali1999@gmail.com"],["Dhyey Bhimani ","dhyeybhimani001@gmail.com"],["Riya Arvind kumar Sonara ","rasonara2002@gmail.com"],["Kevadiya Henil Sanjaybhai","henilkevadiya4518@gmail.com"],["Dhruvrajsinh Mandora","dhruvraj8460@gmail.com"],["ARAB AYESHA","rashidarab44446@gmail.com"],["Viren Zalavadiya","virenzalavadiya01@gmail.com"],["Yash Hindocha ","yashjhindocha@gmail.com"],["Dhairya Joshi","dhairyajoshi.905@gmail.com"],["Krutik Patel","kkrutikk@gmail.com"],["Aditya Brahmbhatt","adityabrahmbhatt62@gmail.com"],["Shashank Muchhadiya ","shashankmj1250@gmail.com"],["Patel Riyan Jagdishbhai","riyanpatel601@gmail.com"],["Krutarth Rindani","rindanikrutarth@gmail.com"],["Sunnykumar v patel","sunny112ce@gmail.com"],["Ravi Parmar","rvparmar1769@gmail.com"],["Mansi Bhavsar ","m18101998@gmail.com"],["Dharmikkumar Bhaveshkumar Patel ","pateldharmik4701@gmail.com"],["Shubhransh Bhargava","shubhranshb240695@gmail.com"],["Heet Patel ","hiitpatel@gmail.com"],["Vivek Modi","vivekmodi2903@gmail.com"],["Nilesh Solanki","nilesh.solanki@embibe.com"],["Hiral Leuva","hirleuva235@gmail.com"],["Hemant Soni","hsoni1010@gmail.com"],["Mohitkumar Bipinchandra Patel ","patelmohit9932@gmail.com"],["Kishan Gehlot ","kishangehlot41@gmail.com"],["PATEL SUJALKUMAR HASMUKHBHAI ","sujalpatel2397@gmail.com"],["Vishal Khanchandani ","vishalhkhanchandani@gmail.com"],["Harsh Dalwadi","dalwadi2@gmail.com"],["Nisarg Vijaybhai Patel","patelnisarg92@gmail.com"],["Rohan Andharia","rohanandharia@gmail.com"],["Arkesh Vijaykumar Kariya","arkeshkariya13@gmail.com"],["Sukhadiya Mitesh Rameshbhai ","miteshpatel0055@gmail.com"],["Soni Binjalben Bhavinkumar","binjalsoni2026@gmail.com"],["Dhairya Shah","dhairyavkshah@gmail.com"],["Nishant yogeshbhai kachhadiya ","nishantpatel4848@gmail.com"],["Ranipa Virag Mansukhbhai","viragranipa7217@gmail.com"],["Hinal Rathod","hinalrathod5@gmail.com"],["Patel ParthKumar Rajendrabhai","patel14193@gmail.com"],["Patel vatsal ashokbhai","vatsalpatel957@gmail.com"],["VISHAL JITENDRABHAI SARVAIYA ","sarvaiyavishal704@gmail.com"],["Maitri Rathod ","maitrirathod2606@gmail.com"],["Yash Rami","yashrami295@gmail.com"],["Vatsal Mehta ","mehtavatsal22@gmail.com"],["Preet Vijaykumar mistry","preetsuhar2205@gmail.com"],["Omdevsinh Yashpalsinh Zala ","omdevsinh1205@gmail.com"],["Milan Chavda","milan123.chavda@gmail.com"],["Patel Jinesh Satishkumar ","jineshpatel8550@gmail.com"],["Shivang Patel","shivang4572@gmail.com"],["Patel Varshil Kalpeshkumar","varshilpatel7575@gmail.com"],["Chhunchha Manan Mayurbhai ","mananchhunchha456@gmail.com"],["Patel Vishvesh","patelvishvesh100@gmail.com"],["Kachhadiya Vatsal Ketanbhai","vatsalkachhadiya99@gmail.com"],["sanket agrawal","vatskachhadiya@gmail.com"],["Fiza Mansuri","fizamansuri@gmail.com"],["Prushti Bhut","putibhut1997@gmail.com"],["Dr Snehkumar Shahani","snehshahani@gmail.com"],["Harsh Jambukiya ","harshjambukiya75@gmail.com"],["Deep Dharasandiya ","dharsandiyadeep1234@gmail.com"],["Kishan Khirasariya","kishankhirasariya.kk@gmail.com"],["Khushbu Makwana","m.khushbu2012@gmail.com"],["Soham Vyas","sohamvyas73@gmail.com"],["Dhaval chauhan","chauhandhaval44@gmail.com"],["Het Manishbhai Patel","hetlu0306@gmail.com"],["Ajay Shukla","ajayshukla9662@gmail.com"],["Keyur Patel ","kkpatel245@gmail.com"],["Dhvani Parghi ","dhvaniparghi2003@gmail.com"],["Hiral Leuva","hirleuva235@gmail.com"],["Patel Jaykumar Riteshbhai","jay60436@gmail.com"],["Dhruvrajsinh Mandora","dhruvraj8460@gmail.com"],["Ketan Navinbhai Solanki","ketansolanki2712@gmail.com"],["Fiza Ansari","fizu3702@gmail.com"],["Keyur Chaniyara ","keyurchaniyara2001@gmail.com"],["Jain Shreyas Sunilkumar","shreyasjain0912@gmail.com"],["Donda Meet Lallubhai","meetdonda8301@gmail.com"],["Rachana joshi ","rachanajoshi239@gmail.com"],["Prajapati Naresh Vimalbhai ","nareshv2309@gmail.com"],["Sarvaiya Rohit Samatbhai ","rohitsarvaiya9624@gmail.com"],["Arth Trada","tradaarth@gmail.com"],["Yatree Ladani","ynladani14@gmail.com"],["Neh Jain","nehjain.2001@gmail.com"],["Milan S Suthar","milan.764586@gmail.com"],["Khushal Modi","kmodi3130@gmail.com"],["Prashant Mehta ","prashantmehta94@gmail.com"],["Jay N Panchal","jay.panchal1491@gmail.com"],["Patel yatra kamleshkumar ","patelyatra4@gmail.com"],["Sachin dangariya","dangariyasachin@gmail.com"],["Dipak Jadav","dipakjadav310@gmail.com"],["Himanshu Patel","himansupatel1795@gmail.com"],["Vishesh Surendrasinh Rohila ","visheshrohila01@gmail.com"],["Daksh Shah","daksh.shah09@gmail.com"],["Bhagya Niranjanbhai patel","bhagyapatel94@gmail.com"],["Trivedi Dev Priteshkumar ","devtrivedi1609@gmail.com"],["Shalin Donga ","dongashalin@gmail.com"],["Naishad Sutariya","naishadh34@gmail.com"],["Rency Sangani ","rencysangani@gmail.com"],["Nagesh Jayantibhai Patel","np1451995@gmail.com"],["Patel yatra kamleshkumar ","patelyatra4@gmail.com"],["Prashant Mansukhbhai Javia","prashantjavia1810@gmail.com"],["Jenish Kanpariya ","jenishkanpariya05@gmail.com"],["Akshar Adhvaryu ","akshar.adhvaryu@gmail.com"],["Viren Prajapati ","viren.prajapati15@gmail.com"],["PIPALIYA AKASH HARSUKHBHAI ","akashhp9085@gmail.com"],["DISHANT SONI","dishants602@gmail.com"],["Ronak Bharatkumar Patel ","rbpatel1598@gmail.com"],["Deepkumar Panara ","panaradeep972@gmail.com"],["Devarshi Brahmbhatt ","dbrahmbhatt24@gmail.com"],["Dikul B Suryavala","dikul.ee@gmail.com"],["PARIKH JOYAL","joyal3010@gmail.com"],["Mohitkumar Talreja ","mohittalreja57@gmail.com"],["Patel Shivam Kiritbhai","shivamkpatel26@gmail.com"],["Jenis Patel","jenis1905patel@gmail.com"],["Parth Pat","parthppatel361@gmail.com"],["Dhruvang Suthar ","dhruvang1992@gmail.com"],["Desai falgunkumar arvindbhai","falgunarvinddesai1234@gmail.com"],["YASH KALPESHKUMAR PATEL","yashkpatel2910@gmail.com"],["Bandish Gopalbhai Panchal ","bandishpanchal@gmail.com"],["Jay Patel ","bandishpanchal@gmail.com"],["Tirth Pareshbhai Patel ","bandishpanchal@gmail.com"],["Harshil Trivedi","trivediharshil75@gmail.com"],["Aditya Vyas ","adityavyas105@gmail.com"],["Chauhan Ileshkumar","ileshchauhan1111@gmail.com"],["Parmar Divyank","parmardivyank56@gmail.com"],["darshil prajapati","darshilprj11@gmail.com"],["Gautamsinh Champavat ","gautamsinhchampavat@gmail.com"],["PARTH PANCHAL","panchalparth00@gmail.com"],["Tejal Gamit ","tejalgamit010@gmail.com"],["Harsh Shah","harshshah2379@gmail.com"],["Dhruv vyas ","dhruvvyas660@gmail.com"],["Yash Priyadarshi ","yashpriyadarshi2@gmail.com"],["Vivek Sharma","theviveksharmaa@gmail.com"],["Meet Bimal Khambhati","meetkhambhati@gmail.com"],["Patel Dhaval Rageshkumar ","pateldhaval24092001@gmail.com"],["Kothari Sakshi Manishkumar","vinnykothari999@gmail.com"],["Purav Dave ","puravdave31@gmail.com"],["Patel Urpitkumar Bhupendrabhai","urpitpatel6002@gmail.com"],["Diwan pruthil ","priyansudiwan11@gmail.com"],["Sudhagar Mudaliar ","mudaliyarsudhagar30@gmail.com"],["Tejas Patel","tejaspatel241289@gmail.com"],["Kartik Patel","kartikpatel@vpmp.ac.in"],["Krishnarajsinh zala","krs778899@gmail.com"],["Patel Prantkumar Ramnikbhai ","prantpatel159@gmail.com"],["Sagar","sagarpatel0203@gmail.com"],["Joy Chauhan","joychauhan98@gmail.com"],["Abhishek Jain","itsabhisworld@gmail.com"],["Pinjal Bamkesh Patel","pinjalmech@gmail.com"],["Mitanshu Kansara","mitanshukansara@gmail.com"],["Sandip godse","sandipgodse1988@gmail.com"],["Maharshi Shah","maharshi.shah1989@gmail.com"],["M A KHORAJIYA ","khorajiyamaksud@gmail.com"],["Gajjar Prem Hitendra ","prem.gajjar07@gmail.com"],["Dr. Dinesh Mevada","write24dinesh@gmail.com"],["Dabhi jaspalsinh b","jaspalsinh@gmail.com"],["Urmil Raval ","urmilraval65@gmail.com"],["Solanki Devang Manharbhai","devrajput97220@gmail.com"],["Nirajkumar Patel ","nirajkumarme38@gmail.com"],["Pratik Panchal ","pdpanch@gmail.com"],["SANJAYKUMAR D MALI","malisanjay28@gmail.com"],["Solanki Nishant Tribhovanbhai","nikssolanki1510@gmail.com"],["Vraj Patel","vrajpatel5017@gmail.com"],["Parekh Hardik Arvindkumar","hardikparekh.5050@gmail.com"],["Dharmveersinh Thakor","dharmveersinh.td@gmail.com"],["BHAUMIK SHAH","shahbhaumik1989@gmail.com"],["Khandelwal Garvit","kgarvit82@gmail.com"],["Navinkumar Prajapati ","navinprajapati97@gmail.com"],["Raval Krupesh ","krupeshraval43@gmail.com"],["Suraj bali","balisuraj98@gmail.com"],["Tapan Gajjar","tapangajjar7@gmail.com"],["Vasani neel ","nkvasani123@gmail.com"],["Parth Mehta","mehtaparth93@gmail.com"],["KRUNALKUMAR Darji","krunal.kriz@gmail.com"],["Niravkumar Mukeshbhai Desai ","niravdesai712@gmail.com"],["Raj Kanabar","rajkanabar74@gmail.com"],["Nikhil Bhagiya","nikhil19920119@gmail.com"],["Kush J Makadia","kushhaveid@gmail.com"],["Nikunj Shaileshbhai Mehta","mehtanikunj247@gmail.com"],["Taslimarif Ansari","gotu.ansari@gmail.com"],["PATEL NILESHKUMAR SANKABHAI","nileshpatel150@gmail.com"],["Siddhant Sharma ","siddhantshrm508@gmail.com"],["Vijaykumar Patel","patelvijay12007@gmail.com"],["VIJAYSINH UDESINH PARMAR","vijk04061989@gmail.com"],["Kunj Gothi","krp.ahm@gmail.com"],["Juber Gandharv","juber269@gmail.com"],["Ayushi Singh","ayushi2330@gmail.com"],["Dhara Bhut","dhara9896@gmail.com"],["PATEL BHAVIKKUMAR AMRUTLAL","bhavikpatel@vpmp.ac.in"],["Maudip Parikh","maudipparikh@gmail.com"],["HARSHVARDHAN ","hvp.prajapati97@gmail.com"],["Umang Panchal","umangpanchal767@gmail.com"],["Makwana Yash U","yashmakwana26@gmail.com"],["Dhwanil Shah ","dhwanilshah52@gmail.com"],["Bhumik Shah ","bhumik0007@gmail.com"],["Patel Manthan Rajeshkumar ","manthanpatel1947@gmail.com"],["BAGERWAL PARTH KAMLESHBHAI","parthbagerwal43@gmail.com"],["Sanket Patel","sankozalavadi865@gmail.com"],["Chauhan Vikas Dineshsingh ","hardik822001@gmail.com"],["Patil Shivam ","patilshivam231198@gmail.com"],["Dixitkumar Krushnkant Patel ","pateldk12321@gmail.com"],["PATEL HARSHAD K","harshad5968@gmail.com"],["SONARA JAYKUMAR ISHWARBHAI ","jaysonara9610@gmail.com"],["Parmar Bhagyeshkumar Bhikhabhai ","pbhagyesh054@gmail.com"],["TIRKAR HARSH ANANTRAY","harshtirkar@gmail.com"],["Kasif Admani","kasif.admani@gmail.com"]]
        for user in users:
            if not User.objects.filter(username=user[1]).first():
                newUser = User()
                newUser.username = user[1]
                newUser.first_name = user[0]
                newUser.email = user[1]
                newUser.set_password("Ldrp@123")
                newUser.save()
                newProfile = Profile()
                newProfile.user = newUser
                newProfile.foodCoupon2 = uuid.uuid4()
                newProfile.college = "LDRP-ITR"
                newProfile.isAllumni = True
                newProfile.save()
            else:
                userNew = User.objects.filter(username=user[1]).first()
                profile = Profile.objects.filter(user=userNew).first()
                if profile:
                    profile.isAllumni = True
                    profile.foodCoupon2 = uuid.uuid4()
                    profile.save()
                else:
                    newProfile = Profile()
                    newProfile.user = userNew
                    newProfile.foodCoupon2 = uuid.uuid4()
                    newProfile.college = "LDRP-ITR"
                    newProfile.isAllumni = True
                    newProfile.save()
            print(user[0])
        return HttpResponse(json.dumps({"data":"done"}),content_type="application/json")
    else:
        return render(request, "404.html")


def emailSender(subject,reciver,template,link):
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
        html = html.replace("%%link%%", link)
        part = MIMEText(html, 'html')
        msg.attach(part)
        connection.sendmail(sender, reciver, msg.as_string())
    pass

def alluminiEmail(request):
    if request.user.is_authenticated and request.user.is_superuser:
        # users = [["Ajay Shukla","ajayshukla9662@gmail.com"],["Kishan Jogiya","kishanjogiya11@gmail.com"],["Nihar Makwana","niharmakwana46@gmail.com"],["Nikunj Panelia","nikunjpanelia1192@gmail.com"],["Malek Nadeem Ahemad ","nadeemahamed22699@gmail.com"],["Ronak Hareshkumar Desai","ronakdesai92@gmail.com"],["Dr. Ankit D. Oza","ankit.oza30956@paruluniversity.ac.in"],["Harshid Keraliya","harshidkeraliya@gmail.com"],["Jadav Akashkumar Nitinkumar","jadavakashkumar@gmail.com"],["Ashish Makhija","makhija726@gmail.com"],["Sakshi Thekdi ","sakshithekdi@gmail.com"],["Aniket Purohit","aniket9124@gmail.com"],["Mrugesh Patel","patelmrugesh.2892@gmail.com"],["Darshan Bhavsar","darshanbhavsar4.db@gmail.com"],["Arjun Parmar","abarjunofficial@gmail.com"],["Uchit Viramgama","uchitpatel7@gmail.com"],["Sahil Jain","jainsahil624@gmail.com"],["Ashok Mali","ashokmali1999@gmail.com"],["Dhyey Bhimani ","dhyeybhimani001@gmail.com"],["Riya Arvind kumar Sonara ","rasonara2002@gmail.com"],["Kevadiya Henil Sanjaybhai","henilkevadiya4518@gmail.com"],["Dhruvrajsinh Mandora","dhruvraj8460@gmail.com"],["ARAB AYESHA","rashidarab44446@gmail.com"],["Viren Zalavadiya","virenzalavadiya01@gmail.com"],["Yash Hindocha ","yashjhindocha@gmail.com"],["Dhairya Joshi","dhairyajoshi.905@gmail.com"],["Krutik Patel","kkrutikk@gmail.com"],["Aditya Brahmbhatt","adityabrahmbhatt62@gmail.com"],["Shashank Muchhadiya ","shashankmj1250@gmail.com"],["Patel Riyan Jagdishbhai","riyanpatel601@gmail.com"],["Krutarth Rindani","rindanikrutarth@gmail.com"],["Sunnykumar v patel","sunny112ce@gmail.com"],["Ravi Parmar","rvparmar1769@gmail.com"],["Mansi Bhavsar ","m18101998@gmail.com"],["Dharmikkumar Bhaveshkumar Patel ","pateldharmik4701@gmail.com"],["Shubhransh Bhargava","shubhranshb240695@gmail.com"],["Heet Patel ","hiitpatel@gmail.com"],["Vivek Modi","vivekmodi2903@gmail.com"],["Nilesh Solanki","nilesh.solanki@embibe.com"],["Hiral Leuva","hirleuva235@gmail.com"],["Hemant Soni","hsoni1010@gmail.com"],["Mohitkumar Bipinchandra Patel ","patelmohit9932@gmail.com"],["Kishan Gehlot ","kishangehlot41@gmail.com"],["PATEL SUJALKUMAR HASMUKHBHAI ","sujalpatel2397@gmail.com"],["Vishal Khanchandani ","vishalhkhanchandani@gmail.com"],["Harsh Dalwadi","dalwadi2@gmail.com"],["Nisarg Vijaybhai Patel","patelnisarg92@gmail.com"],["Rohan Andharia","rohanandharia@gmail.com"],["Arkesh Vijaykumar Kariya","arkeshkariya13@gmail.com"],["Sukhadiya Mitesh Rameshbhai ","miteshpatel0055@gmail.com"],["Soni Binjalben Bhavinkumar","binjalsoni2026@gmail.com"],["Dhairya Shah","dhairyavkshah@gmail.com"],["Nishant yogeshbhai kachhadiya ","nishantpatel4848@gmail.com"],["Ranipa Virag Mansukhbhai","viragranipa7217@gmail.com"],["Hinal Rathod","hinalrathod5@gmail.com"],["Patel ParthKumar Rajendrabhai","patel14193@gmail.com"],["Patel vatsal ashokbhai","vatsalpatel957@gmail.com"],["VISHAL JITENDRABHAI SARVAIYA ","sarvaiyavishal704@gmail.com"],["Maitri Rathod ","maitrirathod2606@gmail.com"],["Yash Rami","yashrami295@gmail.com"],["Vatsal Mehta ","mehtavatsal22@gmail.com"],["Preet Vijaykumar mistry","preetsuhar2205@gmail.com"],["Omdevsinh Yashpalsinh Zala ","omdevsinh1205@gmail.com"],["Milan Chavda","milan123.chavda@gmail.com"],["Patel Jinesh Satishkumar ","jineshpatel8550@gmail.com"],["Shivang Patel","shivang4572@gmail.com"],["Patel Varshil Kalpeshkumar","varshilpatel7575@gmail.com"],["Chhunchha Manan Mayurbhai ","mananchhunchha456@gmail.com"],["Patel Vishvesh","patelvishvesh100@gmail.com"],["Kachhadiya Vatsal Ketanbhai","vatsalkachhadiya99@gmail.com"],["sanket agrawal","vatskachhadiya@gmail.com"],["Fiza Mansuri","fizamansuri@gmail.com"],["Prushti Bhut","putibhut1997@gmail.com"],["Dr Snehkumar Shahani","snehshahani@gmail.com"],["Harsh Jambukiya ","harshjambukiya75@gmail.com"],["Deep Dharasandiya ","dharsandiyadeep1234@gmail.com"],["Kishan Khirasariya","kishankhirasariya.kk@gmail.com"],["Khushbu Makwana","m.khushbu2012@gmail.com"],["Soham Vyas","sohamvyas73@gmail.com"],["Dhaval chauhan","chauhandhaval44@gmail.com"],["Het Manishbhai Patel","hetlu0306@gmail.com"],["Ajay Shukla","ajayshukla9662@gmail.com"],["Keyur Patel ","kkpatel245@gmail.com"],["Dhvani Parghi ","dhvaniparghi2003@gmail.com"],["Hiral Leuva","hirleuva235@gmail.com"],["Patel Jaykumar Riteshbhai","jay60436@gmail.com"],["Dhruvrajsinh Mandora","dhruvraj8460@gmail.com"],["Ketan Navinbhai Solanki","ketansolanki2712@gmail.com"],["Fiza Ansari","fizu3702@gmail.com"],["Keyur Chaniyara ","keyurchaniyara2001@gmail.com"],["Jain Shreyas Sunilkumar","shreyasjain0912@gmail.com"],["Donda Meet Lallubhai","meetdonda8301@gmail.com"],["Rachana joshi ","rachanajoshi239@gmail.com"],["Prajapati Naresh Vimalbhai ","nareshv2309@gmail.com"],["Sarvaiya Rohit Samatbhai ","rohitsarvaiya9624@gmail.com"],["Arth Trada","tradaarth@gmail.com"],["Yatree Ladani","ynladani14@gmail.com"],["Neh Jain","nehjain.2001@gmail.com"],["Milan S Suthar","milan.764586@gmail.com"],["Khushal Modi","kmodi3130@gmail.com"],["Prashant Mehta ","prashantmehta94@gmail.com"],["Jay N Panchal","jay.panchal1491@gmail.com"],["Patel yatra kamleshkumar ","patelyatra4@gmail.com"],["Sachin dangariya","dangariyasachin@gmail.com"],["Dipak Jadav","dipakjadav310@gmail.com"],["Himanshu Patel","himansupatel1795@gmail.com"],["Vishesh Surendrasinh Rohila ","visheshrohila01@gmail.com"],["Daksh Shah","daksh.shah09@gmail.com"],["Bhagya Niranjanbhai patel","bhagyapatel94@gmail.com"],["Trivedi Dev Priteshkumar ","devtrivedi1609@gmail.com"],["Shalin Donga ","dongashalin@gmail.com"],["Naishad Sutariya","naishadh34@gmail.com"],["Rency Sangani ","rencysangani@gmail.com"],["Nagesh Jayantibhai Patel","np1451995@gmail.com"],["Patel yatra kamleshkumar ","patelyatra4@gmail.com"],["Prashant Mansukhbhai Javia","prashantjavia1810@gmail.com"],["Jenish Kanpariya ","jenishkanpariya05@gmail.com"],["Akshar Adhvaryu ","akshar.adhvaryu@gmail.com"],["Viren Prajapati ","viren.prajapati15@gmail.com"],["PIPALIYA AKASH HARSUKHBHAI ","akashhp9085@gmail.com"],["DISHANT SONI","dishants602@gmail.com"],["Ronak Bharatkumar Patel ","rbpatel1598@gmail.com"],["Deepkumar Panara ","panaradeep972@gmail.com"],["Devarshi Brahmbhatt ","dbrahmbhatt24@gmail.com"],["Dikul B Suryavala","dikul.ee@gmail.com"],["PARIKH JOYAL","joyal3010@gmail.com"],["Mohitkumar Talreja ","mohittalreja57@gmail.com"],["Patel Shivam Kiritbhai","shivamkpatel26@gmail.com"],["Jenis Patel","jenis1905patel@gmail.com"],["Parth Pat","parthppatel361@gmail.com"],["Dhruvang Suthar ","dhruvang1992@gmail.com"],["Desai falgunkumar arvindbhai","falgunarvinddesai1234@gmail.com"],["YASH KALPESHKUMAR PATEL","yashkpatel2910@gmail.com"],["Bandish Gopalbhai Panchal ","bandishpanchal@gmail.com"],["Jay Patel ","bandishpanchal@gmail.com"],["Tirth Pareshbhai Patel ","bandishpanchal@gmail.com"],["Harshil Trivedi","trivediharshil75@gmail.com"],["Aditya Vyas ","adityavyas105@gmail.com"],["Chauhan Ileshkumar","ileshchauhan1111@gmail.com"],["Parmar Divyank","parmardivyank56@gmail.com"],["darshil prajapati","darshilprj11@gmail.com"],["Gautamsinh Champavat ","gautamsinhchampavat@gmail.com"],["PARTH PANCHAL","panchalparth00@gmail.com"],["Tejal Gamit ","tejalgamit010@gmail.com"],["Harsh Shah","harshshah2379@gmail.com"],["Dhruv vyas ","dhruvvyas660@gmail.com"],["Yash Priyadarshi ","yashpriyadarshi2@gmail.com"],["Vivek Sharma","theviveksharmaa@gmail.com"],["Meet Bimal Khambhati","meetkhambhati@gmail.com"],["Patel Dhaval Rageshkumar ","pateldhaval24092001@gmail.com"],["Kothari Sakshi Manishkumar","vinnykothari999@gmail.com"],["Purav Dave ","puravdave31@gmail.com"],["Patel Urpitkumar Bhupendrabhai","urpitpatel6002@gmail.com"],["Diwan pruthil ","priyansudiwan11@gmail.com"],["Sudhagar Mudaliar ","mudaliyarsudhagar30@gmail.com"],["Tejas Patel","tejaspatel241289@gmail.com"],["Kartik Patel","kartikpatel@vpmp.ac.in"],["Krishnarajsinh zala","krs778899@gmail.com"],["Patel Prantkumar Ramnikbhai ","prantpatel159@gmail.com"],["Sagar","sagarpatel0203@gmail.com"],["Joy Chauhan","joychauhan98@gmail.com"],["Abhishek Jain","itsabhisworld@gmail.com"],["Pinjal Bamkesh Patel","pinjalmech@gmail.com"],["Mitanshu Kansara","mitanshukansara@gmail.com"],["Sandip godse","sandipgodse1988@gmail.com"],["Maharshi Shah","maharshi.shah1989@gmail.com"],["M A KHORAJIYA ","khorajiyamaksud@gmail.com"],["Gajjar Prem Hitendra ","prem.gajjar07@gmail.com"],["Dr. Dinesh Mevada","write24dinesh@gmail.com"],["Dabhi jaspalsinh b","jaspalsinh@gmail.com"],["Urmil Raval ","urmilraval65@gmail.com"],["Solanki Devang Manharbhai","devrajput97220@gmail.com"],["Nirajkumar Patel ","nirajkumarme38@gmail.com"],["Pratik Panchal ","pdpanch@gmail.com"],["SANJAYKUMAR D MALI","malisanjay28@gmail.com"],["Solanki Nishant Tribhovanbhai","nikssolanki1510@gmail.com"],["Vraj Patel","vrajpatel5017@gmail.com"],["Parekh Hardik Arvindkumar","hardikparekh.5050@gmail.com"],["Dharmveersinh Thakor","dharmveersinh.td@gmail.com"],["BHAUMIK SHAH","shahbhaumik1989@gmail.com"],["Khandelwal Garvit","kgarvit82@gmail.com"],["Navinkumar Prajapati ","navinprajapati97@gmail.com"],["Raval Krupesh ","krupeshraval43@gmail.com"],["Suraj bali","balisuraj98@gmail.com"],["Tapan Gajjar","tapangajjar7@gmail.com"],["Vasani neel ","nkvasani123@gmail.com"],["Parth Mehta","mehtaparth93@gmail.com"],["KRUNALKUMAR Darji","krunal.kriz@gmail.com"],["Niravkumar Mukeshbhai Desai ","niravdesai712@gmail.com"],["Raj Kanabar","rajkanabar74@gmail.com"],["Nikhil Bhagiya","nikhil19920119@gmail.com"],["Kush J Makadia","kushhaveid@gmail.com"],["Nikunj Shaileshbhai Mehta","mehtanikunj247@gmail.com"],["Taslimarif Ansari","gotu.ansari@gmail.com"],["PATEL NILESHKUMAR SANKABHAI","nileshpatel150@gmail.com"],["Siddhant Sharma ","siddhantshrm508@gmail.com"],["Vijaykumar Patel","patelvijay12007@gmail.com"],["VIJAYSINH UDESINH PARMAR","vijk04061989@gmail.com"],["Kunj Gothi","krp.ahm@gmail.com"],["Juber Gandharv","juber269@gmail.com"],["Ayushi Singh","ayushi2330@gmail.com"],["Dhara Bhut","dhara9896@gmail.com"],["PATEL BHAVIKKUMAR AMRUTLAL","bhavikpatel@vpmp.ac.in"],["Maudip Parikh","maudipparikh@gmail.com"],["HARSHVARDHAN ","hvp.prajapati97@gmail.com"],["Umang Panchal","umangpanchal767@gmail.com"],["Makwana Yash U","yashmakwana26@gmail.com"],["Dhwanil Shah ","dhwanilshah52@gmail.com"],["Bhumik Shah ","bhumik0007@gmail.com"],["Patel Manthan Rajeshkumar ","manthanpatel1947@gmail.com"],["BAGERWAL PARTH KAMLESHBHAI","parthbagerwal43@gmail.com"],["Sanket Patel","sankozalavadi865@gmail.com"],["Chauhan Vikas Dineshsingh ","hardik822001@gmail.com"],["Patil Shivam ","patilshivam231198@gmail.com"],["Dixitkumar Krushnkant Patel ","pateldk12321@gmail.com"],["PATEL HARSHAD K","harshad5968@gmail.com"],["SONARA JAYKUMAR ISHWARBHAI ","jaysonara9610@gmail.com"],["Parmar Bhagyeshkumar Bhikhabhai ","pbhagyesh054@gmail.com"],["TIRKAR HARSH ANANTRAY","harshtirkar@gmail.com"],["Kasif Admani","kasif.admani@gmail.com"]]
        users = [["Vishal Barot","vishal_ce@ldrp.ac.in"]]
        for user in users:
            tempUser = User.objects.filter(username=user[1]).first()
            tempProfile  = Profile.objects.filter(user=tempUser).first()
            emailSender("Comprehensive Schedule and Food Coupon - LDRP Alumni Meet 2024",user[1],"./emailTemplates/alumini.html","https://xenesis.ldrp.ac.in/alumini/foodCoupon/"+tempProfile.foodCoupon2)
            print(user[1])
        return HttpResponse("done")
    else:
        return HttpResponse("Not Allowed")

# import base64
# def correctLinker(request):
#     if request.user.is_authenticated and request.user.is_superuser:
#         with open("./Starred.mbox","r") as f:
#             data = f.read()
#             data = data.split("From ")[1:]
#             count = 0
#             for mail in data:
#                 try:
#                     userEmail = mail.split("for <")[1].split(">")[0]
#                     emailContentBase64 = mail.split("Content-Transfer-Encoding: base64\n")[1].split("\n\n--===============")[0]
#                     emailContent = base64.b64decode(emailContentBase64).decode("utf-8")
#                     uuidData = emailContent.split("alumini/foodCoupon/")[1].split('"')[0]
#                     print(userEmail,uuidData)
#                     user = User.objects.filter(username=userEmail).first()
#                     profile = Profile.objects.filter(user=user).first()
#                     profile.foodCoupon2 = uuidData
#                     profile.save()
#                     count += 1
#                 except:
#                     pass
#             print(count)