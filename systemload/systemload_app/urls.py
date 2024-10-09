from django.contrib import admin
from django.urls import path

from . import views

app_name = "systemload_app"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.system_dashboard, name='system_dashboard'),
]