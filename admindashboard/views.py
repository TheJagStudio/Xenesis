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
            # volunteers = ["aditibhalala0820@gmail.com","1054jaypatel@gmail.com","1274vrajsuthar@gmail.com","12harsh2022@gmail.com","283tishyapatel@gmail.com","5611aasthamakwana@gmail.com","767vashishthdesai@gmail.com","Hitpatel5114@gmail.com","Janvi271203@gmail.com","Jeetpateljp2612@gmail.com","Jensichangani400@gmail.com","Krishnapithiya58@gmail.com","Maulipatel2904@gmail.com","Meetmavada023@gmail.com","Meetpavaya@gmail.com","Patelarpit4982@gmail.com","Patelkrinalb9999@gmail.com","Patelmeet1323@gmail.com","Patelprimal4796@gmail.com","Pkp20500@gmail.com","Prachi.patel703@gmail.com","Pratikdabhi436@gmail.com","Shaileshvaniya2586@gmail.com","Suchi3010patel@gmail.com","Suhaniprajapati3105@gmail.com","Vashishthapatel0@gmail.com","Vibhathakkar27@gmail.com","aachalspatel784@gmail.com","aakanksha1615@gmail.com","aasthapatel16244@gmail.com","aasthapatel6244@gmail.com","aastharathod2112@gmail.com","aayushi0708patel@gmail.com","abhi_22016@ldrp.ac.in","acharyamanvay@gmail.com","adit28012004@gmail.com","aditi_22014@ldrp.ac.in","aditipatel1705@gmail.com","aditispatel2020@gmail.com","aditispatel2020@gmail.com ","aeshvi309@gmail.com","aeswapatel@gmail.com","agaraparam@gmail.com","agniveshpatel1910@gmail.com","aishuraj633@gmail.com","aishwaryzaveri@gmail.com","akolatarang@gmail.com","akshparikhak28@gmail.com","alimalek28220@gmail.com","amanafasna3@gmail.com","amanafsana3@gmail.com","amitparmar2901@gmail.com","anagh0106@gmail.com","anirudh2003sharma@gmail.com","anjalee2710@gmail.com","anshudeloli2006@gmail.com","arinprajapati11@gmail.com","arjunlatiwala@gmail.com","arpitrathod252005@gmail.com","arshi4299@gmail.com","arthdarji12@gmail.com","artisolanki222003@gmail.com","aryanrathod410@gmail.com","asheetirpatel@gmail.com","ashwishah1808@gmail.com","axatpatel9824@gmail.com","ayush4sharmaji@gmail.com","ayushipatel5258@gmail.com","ayushsolanki0607@gmail.com","ayushsolanki78716@gmail.com","bansharipatel6595@gmail.com","bansi0341@gmail.com","bbmathurani@gmail.. co.","belanihetvi@gmail.com","bhadanianeel@gmail.com","bhattkrishna0908@gmail.com","bhattkush2170@gmail.com","bhavsardaksh19@gmail.com","bhavyp536@gmail.com","bhumisonghelani@gmail.com","bp8871051@gmail.com","brijkumbhani162@gmail.com","charitreyas@gmail.com","charmi.padh030206@gmail.com","charvimangukiya@gmail.com","chaudharimayur198@gmail.com","chaudharivaibhu18@gmail.com","chaudharymayur198@gmail.com","chaudharyperin4@gmail.com","chetanmeena0811@gmail.com","chiragvadhel29@gmail.com","chothanihasti15@gmail.com","contact.jay.galaxy@gmail.com","d.p.patel2842005@gmail.com","daivikp40@gmail.com","darmik.y.dhanki@gmail.com","darshangoswami229@gmail.com","darshanpatel15105@gmail.com","datardimohsinali@gmail.com","davehardh18@gmail.com","dbjotaniya7806@gmail.com","dbpanchal24@gmail.com","deepajayasri@gmail.com","devanshgajjar04@gmail.com","devanshimodi3112@gmail.com","devanshipatel497@gmail.com ","devanshipatel7414@gmail.com","devanshraval05@gmail.com","devarshisoni28@gmail.com","devinpatel0910@gmail.com","devjani1454@gmail.com","devkipatel10e4@gmail.com","devp1866@gmail.com","devpatel2189@gmail.com","dewanisolanki123@gmail.com","dhairyakanani0602@gmail.com","dhararuparel16@gmail.com","dharmishthabavaghela06@gmail.com","dharmisthabavaghela06@gmail.com","dharmisthapanda66@ gmail. Com","dharmisthapanda66@gmail.com","dharmpatel4284@gmail.com","dharmshayara@gmail.com","dharmshyara@gmail.com","dhavalshapariya7693@gmail.com","dhawanshah.07@gmail.com","dheerdarji1212@gmail.com","dhrumichaudhari72@gmail.com","dhrumip246@gmail.com ","dhruv13542virtual@gmail.com","dhruvilbavarva@gmail.com","dhruvisomaiya9@gmail.com","dhruvjain20102004@gmail.com","dhruvmakwana0165@gmail.com","dhruvmedatiya2004@gmail.com","dhruvpatel.gnr@gmail.com","dhruvshingod01@gmail.com","dhruvtrivedi357@gmail.com","dhruvvaghela1673@gmail.com","dhvani.s.patel30@gmail.com","dhyanagondaliya24@gmail.com","dhyanikhatrani41@gmail.com","disargi11@gmail.com","dishant.asodiya12@gmail.com","dishapatel3951@gmail.com","dishikamistry@gmail.com","divyabalchandani123@gmail.com","divyanhjain@gmail.com","divyanshgopal474@gmail.com","divyapatel2653@gmail.com","divyarathod2292002@gmail.com","divyasolanki7373@gmail.com","divyeshvadher782@gmail.com","diwandarshil1804@gmail.com","diyatrivedi05@gmail.com","djfresh2314@gmail.com","djpandya1901@gmail.com","dkponkiya2106@gmail.com","dnpatel207@gmail.com","dnpatel207@gmail.com ","drashtimankad1@gmail.com","drashtimankadi@gmail.com","drpatel10122005@gmail.com","druv13542vertual@gmail.com","druvmakavana0165@gmail.com","dvpatel168@gmail.com","dvpatel168@gmail.com ","ektavora0708@gmail.com","fenaj105@gmail.com","frefithgohel90@gmail.com","gajjarjuhi66@gmail.com","garalapreet@gmail.com","gargkritika2017@gmail.com","godhaniprinsi0@gmail.com","gorom627@gmail.com","hadiyalhj66@gmail.com","hani_21352@ldrp.ac.in","hanupatel2216@gmail.com","happygnr04@gmail.com ","happysuva@gmail.com","harahpatel.hrp2002@gmail.com","hardirajpara22@gmail.com","hardpatel956519@gmail.com","harmi.patel3200@gmail.com","harsh.patel081004@gmail.com","harshdhameliya3132004@gmail.com","harshilthakkar163@gmail.com","harshilvaliya40@gmail.com","harshpatel080503@gmail.com","harshpatel71761@gmail.com","harshsonaiya09@gmail.com","hastijk83@gmail.com","hayanpatel9104@gmail.com","hc2643405@gmail.com","heathenova2021@gmail.com","heeratit14@gmail.com","heerpatel0511@gmail.com","heeru2501@gmail.com","heetmistry22903@gmail.com","heetpandya14@gmail.com","heleepatel001@gmail.com","hemladani4331@gmail.com","het_22012@ldrp.ac.in","hetbhat10@gmail.com","hetchauhan66@gmail.com","hetp3286@gmail.com","hetpatel6979@gmail.com","hetvikavathiya006@gmail.com","himalikhant@gmail.com","hingrajiyavishva@gmail.com","hiralahir1104@gmail.com","hirenchaudhary909@gmail.com","honeykhanesa@gmail.com","hp333854@gmail.com","hspatel1092004@gmail.com","hypatel0808@gmail.com","irasama01@gmail.com","isha012savaliya@gmail.com","jadavjuhi2406@gmail.com","jagratpatel99@gmail.com","jainampatel5544@gmail.com","jainilprajapati491@gmail.com","jainu2426@gmail.com","janiisha10@gmail.com","janmajeynathvani@gmail.com","jay135827@gmail.com","jay_22220@ldrp.ac.in","jaydeepkhandla11@gmail.com","jayp73922@gmail.com","jder612@gmail.com","jeelbathani11@gmail.com","jeelpopat1010@gmail.com","jenishpatel2286@gmail.com","jimitramani007@gmail.com","joshividhi802@gmail.com","jumangsinh1016@gmail.com","kabirb1612@gmail.com","kandarp.gajjar.460@gmail.com","kandarpjoshi0809@gmail.com ","kandarpmojidra@gmail.com","kanvipatel46@gmail.com","kanzariyagautam12345@gmail.com","karanpatodi99@gmail.com","kashish.savaliya16@gmail.com","katariyavaishali12@gmail.com","kathanparikh13@gmail.com","kathanpatel2020@gmail.com","kauranidivya@gmail.com","kaushal151131@gmail.com","kausharmansuri17@gmail.com","kavy8955@gmail.com","kavyaptl146612@gmail.com","kavyaraj0205@gmail.com","keshvijarsania198@gmail.com","khodbhayadenisa@gmail.com","khuntdhruv007kdj@gmail.com","khushaliparmar934@gmail.com","khushbunathvani7@gmail.com","khushi0630shah@gmail.com","khushi122004@gmail.com","khushijhala3919@gmail.com","khushijoshi969@gmail.com","khushipatelkalipura@gmail.com","khushisom1105@gmail.com","kirthikasundari4@gmail.com","kishanpatidar2004@gmail.com","knp2040@gmail.com","kp892004@gmail.com","kppatel5077@gmail.com","kreshiviroja487@gmail.com","krima_22113@ldrp.ac.in","krinapokiya2311@gmail.com","krishamangukiya0281@gmail.com","krishamodha2004@gmail.com","krishbathani3225@gmail.com","krishna15906@gmail.com","krishnabhanushali2002@gmail.com","krishnamangukiya0281@gmail.com","krishpatel2282@gmail.com","krishpatel8403@gmail.com","krishpatelkrp@gmail.com","krupa5103@gmail.com","krupaliahir10@gmail.com","krutijasani5325@gmail.com","krutika8114@gmail.com","krutikgami354@gmail.com","kuldiptalsaniya@gmail.com","kunjp4517@gmail.com","kunjsathavara2003@gmail.com","kunjsherathiya65@gmail.com","kush_22013@ldrp.ac.in","kushal.om30@gmail.com","kushalprajapati3603@gmail.com","lambhajayesh@gmail.com","lightxape@gmail.com","limbchayarutvikrl@gmail.com","luvambadiya@gmail.com","mahekpatel112005@gmail.com","mahekposhiya@gmail.com","mahipatel1422006@gmail.com","mahipatel3202@gmail.com","mahir992535@gmail.com","mahirkalavadia8@gmail.com","maitreypandya02@gamil.com","makgrish104@gmail.com","makwanajanvi54@gmail.com","makwanapriyanka0007@gmail.com","mannp1755@gmail.com","manpatel4906@gmail.com","manthanpatel1422006@gmail.com","manushkapadiya2021@gmail.com","mayurvidhani075@gmail.com","meerasachchade14@gmail.com","meet40167.pm@gmail.com","meetahir0073@gmail.com","meetbarasara06@gmail.com","meetpokal04@gmail.com","meetsutariya@gmail.com","meetthakkar1980@gmail.com","megalgohil31@gmail.com","meghatrivedi170@gmail.com","mehaupadhyay95@gmail.com","mihirkothari0702@gmail.com","mihirpatel012005@gmail.com","mitp4771@gmail.com","mitraselly47@gmail.com","mohnishmoledina@gmail.com","mosampatel040@gmail.com","mranand960@gmail.com","mrjsutariya@gmail.com ","muchhadiyaharshida@gmail.com","mykyadav17112003@gmail.com","naazpathan2997@gmail.com","nahush0279@gmail.com","naimishharkhani2004@gmail.com","naiya4151@gmail.com","nami.nanavati2812@gmail.com","namrajagani1234@gmail.com","namratamonu28k@gmail.com","nancyp9210@gmail.com","nanushubham20@gmail.com","nayanvora111@gmail.com","neditprmar@gmail.com","needitparmar@gmail.com","neelmerja@gmail.com","nehakumari961610@gmail.com","nehalbavaghela888@gmail.com","nehanshishanghani261@gmail.com","nidhipatel2102000@gmail.com","nihuchavda3105@gmail.com ","niketmaradiya@gmail.com","nilaykalathiya@gmail.com","niralidave1326@gmail.com","nisargpadia@gmail.com","nisargpatel2704@gmail.com","nisargpatel4803@gmail.com","nishtha3205@gmail.com","nupurdave03@gamil.com","oumgadani2004@gmail.com","ozadev03@gmail.com","palakdudhat9066@gmail.com","palakparmar5102002@gmail.com","palashrajpara15@gmail.com","palladani23@gmail.com","panarapurva156@gmail.com","panchalaayush98@gmail.com","panchalurvish93@gmail.com","pandyadivya2103@gmail.com","panesarashivam@gmail.com","parmar.yogin04@gmail.com","parmarchaitali81@gamail.com","parmarhardik9931@gmail.com","parmarheli2005@gmail.com","parmarishita512@gmail.com","parmarjuhi279@gmail.com","parmarurvi507@gmail.com","parmaryogin04@gmail.com","parshavshah0504@gmail.com","parshvaprajapati2004@gmail.com","parthkapadiya231@gmail.com","parthmetkar123@gmail.com","parthparmar.mba@gmail.com","parthparmar3586@gmail.com","parva300504@gmail.com","parva_22153@ldrp.ac.in","parvashukla26@gmail.com","paryan9094@gmail.com","patelabhisek7654@gmail.com","patelaksh396@gmail.com","patelamit67020@gmail.com","pateldharm075@gmail.com","pateldharmendra7981@gmail.com","pateldharmik2107@gmail.com","pateldivy4005@gmial.com","patelgg106@gmail.com","patelhardi0704@gmail.com","patelhenu2004@gmail.com","patelkrish1668@gmail.com","patelmeet102005@gmail.com","pateln1810@gmail.com","patelprachi2101@gmail.com","patelpreet793@gmail.com","patelsavan498@gmail.com","pateltirthkumar7@gmail.com","patelurvi408@gmail.com","patelurvi408@gmail.com ","patilkhushal54321@gmail.com","patoliyanandita0701@gmail.com","patoliyavrunda8833@gmaiil.com","pavayameet@gmail.com","pavitrajoshi1903@gmail.com","pdpatel1911@gmail.com","pinalvk0110@gmail.com","pm635923@gmail.com","pmanthan1708@gmail.com","pmeet3692@gmail.com","ppranjal420@gmail.com","praj14320@gmail.com","prajapatikrish132005@gmail.com","prajapatikunj475@gmail.com","prajapatipiyush.2609@gmail.com","prajapativashishtha33@gmail.com","pramb2003@gmail.com","pranjalpatel420@gmail.com","prathampatel1504@gmail.com","prathampatel3424@gmail.com","prathamrpatel2602@gmail.com","pratikjetani14@gmail.com","preetpatel10114@gmail.com","preksham326@gmail.com","preya0712@gmail.com","princegoswami342000@gmail.com","princekukadiya95@gmail.com","princepatel30p5@gmail.com","princypatel2022@gmail.com","prinshu.patel2004@gmail.com","printibamaniya@gmail.com","priyaaa2319@gmail.com","priyanksatani1234@gmail.com","priyanshee.patil@gmail.com","priyanshi9112004@gmail.com","priyanshipatel3612@gmail.com","priyanshisojitra1712@gmail.com","priyanshupatel832@gmail.com","priyavora69@gmail.com","psns4040@gmail.com","purohitbansi09@gmail.com","pushyashah15@gmail.com","rahipatel191@gmail.com","raiyaniharsh5@gmail.com","rajd99504@gmail.com","rajmovaliya08@gmail.com","rajvirupapara1510@gmail.com","rathodsumit1612005@gmail.com","ravaljanvi@gmail.com","ravalkruti301@gmail.com","ravisenjaliya99@gmail.com","rg4631141@gmail.com","ridhampatel2k4@gmail.com","ridhamrathod1205@gmail.com","ridhamshah625@gmail.com","ritikshakotadiya@gmail.com","ritipatel505@gmail.com","riyapatel47677@gmail.com","rojivadiyamayank@gmail.com","ronakgodhani027@gmail.com","ronakpatel0347@gmail.com","roshanisolanki11105@gmail.com","rp4766827@gmail.com","ruchitpitaliya2003@gmail.com","rudhram.jhavari@gmail.com","rudra15406@gmail.com","rudram.jhaveri@gmail.com","rupareliyameet7@gmail.com","rushilpatel2903@gmail.com","rutapatolia2005@gmail.com","rutva1043@gmail.com","rutvip488@gmail.com","sahilsenjaliya1809@gmail.com","sandipmistry08@gmail.com","sanjayedu2004@gmail.com","sanjivmudaliar2311@gmail.com","sankhla.smit@gmail.com","sanvichaudhary311@gmail.com","savaliyatrusha41@gmail.com","sejalvaghela755@gmail.com","sentavishantj@gmail.com","sgbapodara@gmail.com","shahshreysds@gmail.com","shekhnoornoor036@gmail.com","shivampatel635272@gmail.com","shivansh_22043@ldrp.ac.in","shraddhabasolanki67@gmail.com","shreyansh17122004@gmail.com","shreyapatidar1977@gmail.com","shreyvyas2210@gmail.com","shubh13052004@gmail.com","shubhamparikh07@gmail.com","shubhpatel918@gmail.com","shubhvikani13@gmail.com","shyamkaneriya2006@gmail.com","shyamvanjani6633@gmail.com","sikha.singh09jan@gmail.com","sinhaujjwal175@gmail.com","smitjoshi224@gmail.com","smsuthar2520@gmail.com","snehachatwani36@gmail.com","snehajadeja24@gmail.com","sojitradarshitpiyushbhai@gmail.com","sojitrahimani174@gmail.com","solankimihir1210@gmail.com","solankisureshkumar25@gmail.com","sonalyadav04g@gmail.com","sorathiyasahil5656@gmail.com","soumyaditya611@gmail.com","sp4078164@gmail.com","srushti2353@gmail.com","sugampatel410313@gmail.com","sutharharshp04@gmail.com","sutharsamarth16@gmail.com","suva.neeja11@gmail.com","suva.neeja@gmail.com","swaminarayanvatsal@gmail.com","swapanil0704@gmail.com","swetasharma1902@gmail.com","t37sharmakrishnac@gmail.com","tanishqmaheshwari225@gmail.com","taniyaambwani26@gmail.com","thakkarkrutika4@gmail.com","thekrishpatel20@gmail.com","thisisrudrab@gmail.com","tilakpatel2424@gmail.com","tirkardhruv67@gmail.com","tirthacharya97@gmail.com","tirthbhinagradiya1604@gmail.com","tirthchomal@gmail.com","tirthpatel162005@gmail.com","tithu244@gmail.com","tusdrj@gmail.com","udaychanpa101@gmail.com","udaychanpa635@gmail.com","udayvasoya603@gmail.com","upadhyaykinjal050@gmail.com","upadhyayraj918@gmail.com","urjasoni0124@gmail.com","urvii1521@gmail.com","urvish7904@gmail.com","vadaliyatirth@gmail.com","vaghasiyapinal2003@gmail.com","vaghelaastha92@gmail.com","vaghelakrushnadevsinh523@gmail.com","vaghelavijay8347@gmail.com","vaibhavsukhwal1345@gmail.com","vaishnavisoni0307@gmail.com","vanpariyapalak@gmail.com","vanshilrathod9904@gmail.com","varcha108@gmail.com","varshilparejiya2004@gmail.com","vasukpatel025@gmail.com","vasurupapara5@gmail.com","vasuvachhani2004@gmail.com","vedanshldrp3005@gmail.com","vedanthirani99@gmail.com","vedantjoshi2115@gmail.com","vedantshah2401@gmail.com","vikashbaraiya6512@gmail.com","vinitsuva97@gmail.com","viratdharaiya2004@gmail.com","vishvam028@gmail.com","vishvamaradia25072@gmail.com","vishvldrp7@gmail.com","vishwangsuthar.997@gmail.com","vishwasoni11@gmail.com","vishwasonil@gmail.com","vraj_21244@ldrp.ac.in","vrajc494@gmail.com","vrajp1016@gmail.com","vrajshrimali2410@gmail.com","vrajsuthar127@gmail.com","vrund4591@gmail.com","vrushtip19@gmail.com","vrutikap348@gmail.com","vrutvip1330@gmail.com","vyasanjali17@gmail.com","vyascv5714@gmail.com","yagnikjasoliya@gmail.com","yash10876@gmail.com","yashgajjar2222@gmail.com","yashuvithalani21@gmail.com","yp1102003@gmail.com","ypatel6353@gmail.com","yug p9244@gmail.com","yug190705@gmail.com","zadafiyaraj395@gmail.com","zalak552005@gmail.com","zeelkanudawala@gmail.com","zeelsimejiyal6@gmail.com","zenishadevani@gmail.com","ziyanmansuri2112@gmail.com"]
            # for volunteer in volunteers:
            #     user = Profile.objects.filter(user__email=volunteer).first()
            #     if user:
            #         tempUUID = uuid.uuid4()
            #         tempUUID2 = uuid.uuid4()
            #         user.foodCoupon = tempUUID2
            #         user.foodCoupon2 = tempUUID
            #         user.save()
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