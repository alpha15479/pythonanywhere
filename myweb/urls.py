from django.urls import path
from django.contrib.auth import views as aunt_views
from . import views
from . import *

urlpatterns = [
    path('', views.index, name='index'),
    path('login',views.login_page),
    path('signup', views.signup, name='signup'),
    path('logout',views.logout, name='logout'),
    path('login_active',views.login_active),

]