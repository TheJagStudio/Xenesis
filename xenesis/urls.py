from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('api.urls')),
    path('dashboard/', include('admindashboard.urls')),
    path('', include('web.urls')),
    path('admin/', admin.site.urls),
]
