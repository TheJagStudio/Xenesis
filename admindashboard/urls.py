from django.urls import path
from . import views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data', views.data, name='data'),
    path('events', views.events, name='events'),
    path('tableData', views.tableData, name='tableData'),
    path('login', views.singin, name="singin"),

]
