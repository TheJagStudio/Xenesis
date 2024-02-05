from django.contrib import admin
from .models import Profile, Department, Event, Ticket
from import_export.admin import ExportActionMixin


class ProfileAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('user', 'phone', 'college')
    search_fields = ['user__email', 'phone', 'college']


class DepartmentAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name', 'coordinator1', 'coordinator2')
    search_fields = ['name', 'coordinator1__user__email', 'coordinator2__user__email']


class EventAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name','department', 'price','teamPrice',"isTeamEvent")
    search_fields = ['name', 'department__name', 'price','teamPrice',"isTeamEvent"]
    # list_editable = ('isTeamEvent',)
    # list_display_links = ('price',)
    


class TicketAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('id','owner','event','isPaid','isScanned','qrCodeData',  'date')
    search_fields = ['id','owner__user__email', 'event__name','isPaid','isScanned','qrCodeData', 'date']
    list_editable = ('isPaid','isScanned')






admin.site.register(Profile, ProfileAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Ticket, TicketAdmin)