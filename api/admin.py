from django.contrib import admin
from .models import Profile, Department, Event, Ticket, Notifications,Gallery
from import_export.admin import ExportActionMixin


class ProfileAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('user', 'phone', 'college')
    search_fields = ['user', 'phone', 'college']


class DepartmentAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name', 'coordinator1', 'coordinator2')
    search_fields = ['name', 'coordinator1', 'coordinator2']


class EventAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name', 'price', 'location')
    search_fields = ['name',  'price', 'location']


class TicketAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('owner',  'date')
    search_fields = ['owner',  'date']


class NotificationsAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('user',  'dateTime')
    search_fields = ['user',  'dateTime']

class GalleryAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('path',)
    search_fields = ['path']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Notifications, NotificationsAdmin)
admin.site.register(Gallery, GalleryAdmin)
