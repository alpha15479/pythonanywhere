from django.urls import path
from . import views
from . import *

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('login', views.login_page),
    path('show', views.show_page),
    path('Homepage', views.Homepage),
    path('signup', views.signup, name='signup'),
    path('add', views.add_page),
    path('logout',views.logout, name='logout'),
    path('Meat',views.Meat, name='Meat'),
    path('Fruits',views.Fruits, name='Fruits'),
    path('Vegs',views.Vegs, name='Vegs'),
    path('Pong',views.Pong, name='Pong'),
    path('login_active',views.login_active, name='login_active'),
    path('add_model',views.add_model, name='add_model'),
]