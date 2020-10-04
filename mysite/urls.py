from django.contrib import admin
from django.urls import path, include
from myweb import views

urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('Homepage/', views.Homepage),
    path('login/', views.login),
    path('signup/', views.signup),
    path('myweb/', include('myweb.urls')),
    path('united', views.united),
    path('admin/', admin.site.urls),
]
