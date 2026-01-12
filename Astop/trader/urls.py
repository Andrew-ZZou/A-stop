from django.urls import path
from . import views

app_name = 'traders'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('plumbers', views.plumbers, name = 'plumbers'),
    path('details/<int:client_id>', views.details, name = 'details'),
    path('backdoor',views.backdoor,name ='backdoor'),
    path('management', views.management, name = 'management'),
    path('registration', views.registration, name = 'registration'),
    path('login', views.login, name = 'login'),
    path('test', views.test, name = 'test'),
]