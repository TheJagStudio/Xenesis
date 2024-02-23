from django.shortcuts import render

from django.http import HttpResponse
from api.models import Profile, Department, Event, Ticket

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
    return render(request, "index.html")
def events(request):
    return render(request, "index.html")
def eventDetails(request,event):
    return render(request, "index.html")
def myticket(request):
    return render(request, "index.html")
def aboutus(request):
    return render(request, "index.html")
def login(request):
    return render(request, "index.html")
def register(request):
    return render(request, "index.html")
def otp(request):
    return render(request, "index.html")
def accountsetup(request):
    return render(request, "index.html")
def verifier(request):
    return render(request, "index.html")
def EventTicketVerifer(request):
    return render(request, "index.html")
def TicketPaymentVerifer(request):
    return render(request, "index.html")
def FoodCouponVerifer(request):
    return render(request, "index.html")
def faqs(request):
    return render(request, "index.html")
def forgotpassword(request):
    return render(request, "index.html")
def resetpassword(request):
    return render(request, "index.html")
def eventConfirmation(request):
    return render(request, "index.html")
def eventRegistration(request):
    return render(request, "index.html")
def verifiedTickets(request):
    return render(request, "index.html")

def aluminiFoodCoupon(request,coupon):
    users = [["Ajay Shukla","ajayshukla9662@gmail.com"],["Kishan Jogiya","kishanjogiya11@gmail.com"],["Nihar Makwana","niharmakwana46@gmail.com"],["Nikunj Panelia","nikunjpanelia1192@gmail.com"],["Malek Nadeem Ahemad ","nadeemahamed22699@gmail.com"],["Ronak Hareshkumar Desai","ronakdesai92@gmail.com"],["Dr. Ankit D. Oza","ankit.oza30956@paruluniversity.ac.in"],["Harshid Keraliya","harshidkeraliya@gmail.com"],["Jadav Akashkumar Nitinkumar","jadavakashkumar@gmail.com"],["Ashish Makhija","makhija726@gmail.com"],["Sakshi Thekdi ","sakshithekdi@gmail.com"],["Aniket Purohit","aniket9124@gmail.com"],["Mrugesh Patel","patelmrugesh.2892@gmail.com"],["Darshan Bhavsar","darshanbhavsar4.db@gmail.com"],["Arjun Parmar","abarjunofficial@gmail.com"],["Uchit Viramgama","uchitpatel7@gmail.com"],["Sahil Jain","jainsahil624@gmail.com"],["Ashok Mali","ashokmali1999@gmail.com"],["Dhyey Bhimani ","dhyeybhimani001@gmail.com"],["Riya Arvind kumar Sonara ","rasonara2002@gmail.com"],["Kevadiya Henil Sanjaybhai","henilkevadiya4518@gmail.com"],["Dhruvrajsinh Mandora","dhruvraj8460@gmail.com"],["ARAB AYESHA","rashidarab44446@gmail.com"],["Viren Zalavadiya","virenzalavadiya01@gmail.com"],["Yash Hindocha ","yashjhindocha@gmail.com"],["Dhairya Joshi","dhairyajoshi.905@gmail.com"],["Krutik Patel","kkrutikk@gmail.com"],["Aditya Brahmbhatt","adityabrahmbhatt62@gmail.com"],["Shashank Muchhadiya ","shashankmj1250@gmail.com"],["Patel Riyan Jagdishbhai","riyanpatel601@gmail.com"],["Krutarth Rindani","rindanikrutarth@gmail.com"],["Sunnykumar v patel","sunny112ce@gmail.com"],["Ravi Parmar","rvparmar1769@gmail.com"],["Mansi Bhavsar ","m18101998@gmail.com"],["Dharmikkumar Bhaveshkumar Patel ","pateldharmik4701@gmail.com"],["Shubhransh Bhargava","shubhranshb240695@gmail.com"],["Heet Patel ","hiitpatel@gmail.com"],["Vivek Modi","vivekmodi2903@gmail.com"],["Nilesh Solanki","nilesh.solanki@embibe.com"],["Hiral Leuva","hirleuva235@gmail.com"],["Hemant Soni","hsoni1010@gmail.com"],["Mohitkumar Bipinchandra Patel ","patelmohit9932@gmail.com"],["Kishan Gehlot ","kishangehlot41@gmail.com"],["PATEL SUJALKUMAR HASMUKHBHAI ","sujalpatel2397@gmail.com"],["Vishal Khanchandani ","vishalhkhanchandani@gmail.com"],["Harsh Dalwadi","dalwadi2@gmail.com"],["Nisarg Vijaybhai Patel","patelnisarg92@gmail.com"],["Rohan Andharia","rohanandharia@gmail.com"],["Arkesh Vijaykumar Kariya","arkeshkariya13@gmail.com"],["Sukhadiya Mitesh Rameshbhai ","miteshpatel0055@gmail.com"],["Soni Binjalben Bhavinkumar","binjalsoni2026@gmail.com"],["Dhairya Shah","dhairyavkshah@gmail.com"],["Nishant yogeshbhai kachhadiya ","nishantpatel4848@gmail.com"],["Ranipa Virag Mansukhbhai","viragranipa7217@gmail.com"],["Hinal Rathod","hinalrathod5@gmail.com"],["Patel ParthKumar Rajendrabhai","patel14193@gmail.com"],["Patel vatsal ashokbhai","vatsalpatel957@gmail.com"],["VISHAL JITENDRABHAI SARVAIYA ","sarvaiyavishal704@gmail.com"],["Maitri Rathod ","maitrirathod2606@gmail.com"],["Yash Rami","yashrami295@gmail.com"],["Vatsal Mehta ","mehtavatsal22@gmail.com"],["Preet Vijaykumar mistry","preetsuhar2205@gmail.com"],["Omdevsinh Yashpalsinh Zala ","omdevsinh1205@gmail.com"],["Milan Chavda","milan123.chavda@gmail.com"],["Patel Jinesh Satishkumar ","jineshpatel8550@gmail.com"],["Shivang Patel","shivang4572@gmail.com"],["Patel Varshil Kalpeshkumar","varshilpatel7575@gmail.com"],["Chhunchha Manan Mayurbhai ","mananchhunchha456@gmail.com"],["Patel Vishvesh","patelvishvesh100@gmail.com"],["Kachhadiya Vatsal Ketanbhai","vatsalkachhadiya99@gmail.com"],["sanket agrawal","vatskachhadiya@gmail.com"],["Fiza Mansuri","fizamansuri@gmail.com"],["Prushti Bhut","putibhut1997@gmail.com"],["Dr Snehkumar Shahani","snehshahani@gmail.com"],["Harsh Jambukiya ","harshjambukiya75@gmail.com"],["Deep Dharasandiya ","dharsandiyadeep1234@gmail.com"],["Kishan Khirasariya","kishankhirasariya.kk@gmail.com"],["Khushbu Makwana","m.khushbu2012@gmail.com"],["Soham Vyas","sohamvyas73@gmail.com"],["Dhaval chauhan","chauhandhaval44@gmail.com"],["Het Manishbhai Patel","hetlu0306@gmail.com"],["Ajay Shukla","ajayshukla9662@gmail.com"],["Keyur Patel ","kkpatel245@gmail.com"],["Dhvani Parghi ","dhvaniparghi2003@gmail.com"],["Hiral Leuva","hirleuva235@gmail.com"],["Patel Jaykumar Riteshbhai","jay60436@gmail.com"],["Dhruvrajsinh Mandora","dhruvraj8460@gmail.com"],["Ketan Navinbhai Solanki","ketansolanki2712@gmail.com"],["Fiza Ansari","fizu3702@gmail.com"],["Keyur Chaniyara ","keyurchaniyara2001@gmail.com"],["Jain Shreyas Sunilkumar","shreyasjain0912@gmail.com"],["Donda Meet Lallubhai","meetdonda8301@gmail.com"],["Rachana joshi ","rachanajoshi239@gmail.com"],["Prajapati Naresh Vimalbhai ","nareshv2309@gmail.com"],["Sarvaiya Rohit Samatbhai ","rohitsarvaiya9624@gmail.com"],["Arth Trada","tradaarth@gmail.com"],["Yatree Ladani","ynladani14@gmail.com"],["Neh Jain","nehjain.2001@gmail.com"],["Milan S Suthar","milan.764586@gmail.com"],["Khushal Modi","kmodi3130@gmail.com"],["Prashant Mehta ","prashantmehta94@gmail.com"],["Jay N Panchal","jay.panchal1491@gmail.com"],["Patel yatra kamleshkumar ","patelyatra4@gmail.com"],["Sachin dangariya","dangariyasachin@gmail.com"],["Dipak Jadav","dipakjadav310@gmail.com"],["Himanshu Patel","himansupatel1795@gmail.com"],["Vishesh Surendrasinh Rohila ","visheshrohila01@gmail.com"],["Daksh Shah","daksh.shah09@gmail.com"],["Bhagya Niranjanbhai patel","bhagyapatel94@gmail.com"],["Trivedi Dev Priteshkumar ","devtrivedi1609@gmail.com"],["Shalin Donga ","dongashalin@gmail.com"],["Naishad Sutariya","naishadh34@gmail.com"],["Rency Sangani ","rencysangani@gmail.com"],["Nagesh Jayantibhai Patel","np1451995@gmail.com"],["Patel yatra kamleshkumar ","patelyatra4@gmail.com"],["Prashant Mansukhbhai Javia","prashantjavia1810@gmail.com"],["Jenish Kanpariya ","jenishkanpariya05@gmail.com"],["Akshar Adhvaryu ","akshar.adhvaryu@gmail.com"],["Viren Prajapati ","viren.prajapati15@gmail.com"],["PIPALIYA AKASH HARSUKHBHAI ","akashhp9085@gmail.com"],["DISHANT SONI","dishants602@gmail.com"],["Ronak Bharatkumar Patel ","rbpatel1598@gmail.com"],["Deepkumar Panara ","panaradeep972@gmail.com"],["Devarshi Brahmbhatt ","dbrahmbhatt24@gmail.com"],["Dikul B Suryavala","dikul.ee@gmail.com"],["PARIKH JOYAL","joyal3010@gmail.com"],["Mohitkumar Talreja ","mohittalreja57@gmail.com"],["Patel Shivam Kiritbhai","shivamkpatel26@gmail.com"],["Jenis Patel","jenis1905patel@gmail.com"],["Parth Pat","parthppatel361@gmail.com"],["Dhruvang Suthar ","dhruvang1992@gmail.com"],["Desai falgunkumar arvindbhai","falgunarvinddesai1234@gmail.com"],["YASH KALPESHKUMAR PATEL","yashkpatel2910@gmail.com"],["Bandish Gopalbhai Panchal ","bandishpanchal@gmail.com"],["Jay Patel ","bandishpanchal@gmail.com"],["Tirth Pareshbhai Patel ","bandishpanchal@gmail.com"],["Harshil Trivedi","trivediharshil75@gmail.com"],["Aditya Vyas ","adityavyas105@gmail.com"],["Chauhan Ileshkumar","ileshchauhan1111@gmail.com"],["Parmar Divyank","parmardivyank56@gmail.com"],["darshil prajapati","darshilprj11@gmail.com"],["Gautamsinh Champavat ","gautamsinhchampavat@gmail.com"],["PARTH PANCHAL","panchalparth00@gmail.com"],["Tejal Gamit ","tejalgamit010@gmail.com"],["Harsh Shah","harshshah2379@gmail.com"],["Dhruv vyas ","dhruvvyas660@gmail.com"],["Yash Priyadarshi ","yashpriyadarshi2@gmail.com"],["Vivek Sharma","theviveksharmaa@gmail.com"],["Meet Bimal Khambhati","meetkhambhati@gmail.com"],["Patel Dhaval Rageshkumar ","pateldhaval24092001@gmail.com"],["Kothari Sakshi Manishkumar","vinnykothari999@gmail.com"],["Purav Dave ","puravdave31@gmail.com"],["Patel Urpitkumar Bhupendrabhai","urpitpatel6002@gmail.com"],["Diwan pruthil ","priyansudiwan11@gmail.com"],["Sudhagar Mudaliar ","mudaliyarsudhagar30@gmail.com"],["Tejas Patel","tejaspatel241289@gmail.com"],["Kartik Patel","kartikpatel@vpmp.ac.in"],["Krishnarajsinh zala","krs778899@gmail.com"],["Patel Prantkumar Ramnikbhai ","prantpatel159@gmail.com"],["Sagar","sagarpatel0203@gmail.com"],["Joy Chauhan","joychauhan98@gmail.com"],["Abhishek Jain","itsabhisworld@gmail.com"],["Pinjal Bamkesh Patel","pinjalmech@gmail.com"],["Mitanshu Kansara","mitanshukansara@gmail.com"],["Sandip godse","sandipgodse1988@gmail.com"],["Maharshi Shah","maharshi.shah1989@gmail.com"],["M A KHORAJIYA ","khorajiyamaksud@gmail.com"],["Gajjar Prem Hitendra ","prem.gajjar07@gmail.com"],["Dr. Dinesh Mevada","write24dinesh@gmail.com"],["Dabhi jaspalsinh b","jaspalsinh@gmail.com"],["Urmil Raval ","urmilraval65@gmail.com"],["Solanki Devang Manharbhai","devrajput97220@gmail.com"],["Nirajkumar Patel ","nirajkumarme38@gmail.com"],["Pratik Panchal ","pdpanch@gmail.com"],["SANJAYKUMAR D MALI","malisanjay28@gmail.com"],["Solanki Nishant Tribhovanbhai","nikssolanki1510@gmail.com"],["Vraj Patel","vrajpatel5017@gmail.com"],["Parekh Hardik Arvindkumar","hardikparekh.5050@gmail.com"],["Dharmveersinh Thakor","dharmveersinh.td@gmail.com"],["BHAUMIK SHAH","shahbhaumik1989@gmail.com"],["Khandelwal Garvit","kgarvit82@gmail.com"],["Navinkumar Prajapati ","navinprajapati97@gmail.com"],["Raval Krupesh ","krupeshraval43@gmail.com"],["Suraj bali","balisuraj98@gmail.com"],["Tapan Gajjar","tapangajjar7@gmail.com"],["Vasani neel ","nkvasani123@gmail.com"],["Parth Mehta","mehtaparth93@gmail.com"],["KRUNALKUMAR Darji","krunal.kriz@gmail.com"],["Niravkumar Mukeshbhai Desai ","niravdesai712@gmail.com"],["Raj Kanabar","rajkanabar74@gmail.com"],["Nikhil Bhagiya","nikhil19920119@gmail.com"],["Kush J Makadia","kushhaveid@gmail.com"],["Nikunj Shaileshbhai Mehta","mehtanikunj247@gmail.com"],["Taslimarif Ansari","gotu.ansari@gmail.com"],["PATEL NILESHKUMAR SANKABHAI","nileshpatel150@gmail.com"],["Siddhant Sharma ","siddhantshrm508@gmail.com"],["Vijaykumar Patel","patelvijay12007@gmail.com"],["VIJAYSINH UDESINH PARMAR","vijk04061989@gmail.com"],["Kunj Gothi","krp.ahm@gmail.com"],["Juber Gandharv","juber269@gmail.com"],["Ayushi Singh","ayushi2330@gmail.com"],["Dhara Bhut","dhara9896@gmail.com"],["PATEL BHAVIKKUMAR AMRUTLAL","bhavikpatel@vpmp.ac.in"],["Maudip Parikh","maudipparikh@gmail.com"],["HARSHVARDHAN ","hvp.prajapati97@gmail.com"],["Umang Panchal","umangpanchal767@gmail.com"],["Makwana Yash U","yashmakwana26@gmail.com"],["Dhwanil Shah ","dhwanilshah52@gmail.com"],["Bhumik Shah ","bhumik0007@gmail.com"],["Patel Manthan Rajeshkumar ","manthanpatel1947@gmail.com"],["BAGERWAL PARTH KAMLESHBHAI","parthbagerwal43@gmail.com"],["Sanket Patel","sankozalavadi865@gmail.com"],["Chauhan Vikas Dineshsingh ","hardik822001@gmail.com"],["Patil Shivam ","patilshivam231198@gmail.com"],["Dixitkumar Krushnkant Patel ","pateldk12321@gmail.com"],["PATEL HARSHAD K","harshad5968@gmail.com"],["SONARA JAYKUMAR ISHWARBHAI ","jaysonara9610@gmail.com"],["Parmar Bhagyeshkumar Bhikhabhai ","pbhagyesh054@gmail.com"],["TIRKAR HARSH ANANTRAY","harshtirkar@gmail.com"],["Kasif Admani","kasif.admani@gmail.com"]]
    for user in users:
        emailSender("Xenesis Food Coupon",user[1],"templates/foodCoupon.html",coupon)
    return render(request, "index.html")