from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    path('backdoor', views.backdoor, name = "backdoor"),
    path('management', views.management, name = 'management'),
]