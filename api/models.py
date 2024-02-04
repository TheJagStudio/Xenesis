from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    def default_data():
        return {"data": []}
    def location_data():
        return {"lat": 0, "lng": 0,"ip":""}

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="User")
    profilePic = models.CharField(max_length=100, default="0001")
    phone = models.CharField(max_length=10, blank=True)
    otp = models.CharField(max_length=6, blank=True)
    isVolunteer = models.BooleanField(default=False)
    isOrganiser = models.BooleanField(default=False)
    isAccountSetup = models.BooleanField(default=False)
    isCampainVolunteer = models.BooleanField(default=False)
    isVerified = models.BooleanField(default=False)    
    college = models.CharField(max_length=500, blank=True)
    foodCoupon = models.CharField(max_length=64, blank=True)
    isScannedCoupon = models.BooleanField(default=False)
    location = models.JSONField(default=location_data)

    def __str__(self):
        return str(self.user.username)


class Department(models.Model):
    name = models.CharField(max_length=500, unique=True)
    abbriviation = models.CharField(max_length=10, default="")
    coordinator1 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='department_coordinator1')
    coordinator2 = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, related_name='department_coordinator2')
    posterImage = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.name)


class Event(models.Model):
    def default_images():
        return {"data": ["/static/event-images/1.jpg","/static/event-images/2.jpg","/static/event-images/3.jpg","/static/event-images/4.jpg"]}
    name = models.CharField(max_length=500, unique=True)
    link = models.CharField(max_length=500, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    teamName = models.CharField(max_length=100)
    teamLeader = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="event_teamLeader")
    price = models.CharField(max_length=10, default="-")
    teamPrice = models.CharField(max_length=10, default="-")
    winnerPrice1 = models.CharField(max_length=10, null=True, blank=True)
    winnerPrice2 = models.CharField(max_length=10, null=True, blank=True)
    winnerPrice3 = models.CharField(max_length=10, null=True, blank=True)
    location = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    rules = models.CharField(max_length=10000, null=True, blank=True)
    round1Title = models.CharField(max_length=200, null=True, blank=True)
    round1 = models.CharField(max_length=10000, null=True, blank=True)
    round2Title = models.CharField(max_length=200, null=True, blank=True)
    round2 = models.CharField(max_length=10000, null=True, blank=True)
    round3Title = models.CharField(max_length=200, null=True, blank=True)
    round3 = models.CharField(max_length=10000, null=True, blank=True)
    round4Title = models.CharField(max_length=200, null=True, blank=True)
    round4 = models.CharField(max_length=10000, null=True, blank=True)
    round5Title = models.CharField(max_length=200, null=True, blank=True)
    round5 = models.CharField(max_length=10000, null=True, blank=True)
    tagline = models.CharField(max_length=2000)
    posterImage = models.CharField(max_length=1000)
    organiser1 = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True,null=True, related_name='organiser1_event')
    organiser2 = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True,null=True, related_name='organiser2_event')
    organiser3 = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True,null=True, related_name='organiser3_event')
    organiser4 = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True,null=True, related_name='organiser4_event')
    organiser5 = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True,null=True, related_name='organiser5_event')
    teamParticapantCount = models.PositiveIntegerField(default=1)
    teamParticapantCountMin = models.PositiveIntegerField(default=1)
    isTeamEvent = models.BooleanField()
    isTeamPriceFull  = models.BooleanField(default=False)
    isClosed = models.BooleanField()
    status = models.CharField(max_length=100)
    images = models.JSONField(default=default_images)

    def __str__(self):
        return str(self.name)


class Ticket(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    owner1 = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True,related_name="owner1_ticket")
    owner2 = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True,related_name="owner2_ticket")
    owner3 = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True,related_name="owner3_ticket")
    owner4 = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True,related_name="owner4_ticket")
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    comments = models.CharField(max_length=200,null=True,blank=True)
    date = models.DateField(auto_now_add=True)
    qrCodeData = models.CharField(max_length=64)
    userCount = models.PositiveIntegerField(default=1)
    paymentMethod = models.CharField(max_length=100,null=True,blank=True)
    isScanned = models.BooleanField(default=False)
    isPaid = models.BooleanField(default=False)
    acceptedBy = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True,blank=True,related_name="name_acceptedBy") 
    def __str__(self):
        return str(self.owner) and str(self.event)
