from django.contrib import admin
from .models import Profile, Department, Event, Ticket
from import_export.admin import ExportActionMixin
from import_export import resources


class ProfileAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('user', 'phone', 'college','isVolunteer','isOrganiser','isCampainVolunteer')
    search_fields = ['user__email', 'phone', 'college','isVolunteer','isOrganiser','isCampainVolunteer']
    list_filter = ('isVolunteer','isOrganiser','isCampainVolunteer')


class DepartmentAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name', 'coordinator1', 'coordinator2')
    search_fields = ['name', 'coordinator1__user__email', 'coordinator2__user__email']


class EventAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name','department', 'isClosed',"isTeamEvent")
    search_fields = ['name', 'department__name', 'isClosed',"isTeamEvent"]
    list_editable = ( 'isClosed',)
    list_filter = ('isClosed',"isTeamEvent")
    # list_display_links = ('price',)
    

class TicketResource(resources.ModelResource):
    class Meta:
        model = Ticket

    def before_export(self, queryset, *args, **kwargs):
        for obj in queryset:
            obj.owner = obj.owner.user.username
            obj.owner1 = obj.owner1.user.username if obj.owner1 else None
            obj.owner2 = obj.owner2.user.username if obj.owner2 else None
            obj.owner3 = obj.owner3.user.username if obj.owner3 else None
            obj.owner4 = obj.owner4.user.username if obj.owner4 else None
            obj.event = obj.event.name
            obj.acceptedBy = obj.acceptedBy.user.username if obj.acceptedBy else None

class TicketAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = TicketResource
    list_display = ('id','owner','event','isPaid','isScanned','qrCodeData',  'date')
    search_fields = ['id','owner__user__email', 'event__name','isPaid','isScanned','qrCodeData', 'date']
    list_editable = ('isPaid','isScanned')
    list_filter = ('isPaid','isScanned')
    






admin.site.register(Profile, ProfileAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Ticket, TicketAdmin)