from django.urls import path
from . import views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data', views.data, name='data'),
    path('events', views.events, name='events'),
    path('tableData', views.tableData, name='tableData'),
    path('map', views.map, name="map"),
    path('godMode', views.godMode, name="godMode"),
    path('dataMaker', views.dataMaker, name="dataMaker"),
    path('foodEater', views.foodEater, name="foodEater"),
    path('memberPerEvent', views.memberPerEvent, name="memberPerEvent"),
    path('isOrganiserEater', views.isOrganiserEater, name="isOrganiserEater"),
]
