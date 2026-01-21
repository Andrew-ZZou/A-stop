from django.urls import path
from . import views

app_name = 'trader'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('plumber', views.plumber, name = 'plumber'),
    path('electrician', views.electrician, name = 'electrician'),
    path('handyman', views.handyman, name = 'handyman'),
    path('details/<client_id>', views.details, name = 'details'),
    path('registration/', views.registration, name = 'registration'),
    path('login/', views.login, name = 'login'),
    path('promo_edit/<client_id>', views.promo_edit, name = 'promo_edit'),
    path('search/', views.search, name = 'search'),
    path('test', views.test, name = 'test'),
]