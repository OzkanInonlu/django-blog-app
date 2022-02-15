from django.contrib import admin
from django.urls import path

from blog import settings
from . import views
from django.conf.urls.static import static

app_name = "user"

urlpatterns = [
    path('register/', views.register, name = "register"),
    path('login/', views.loginUser, name = "login"),
    path('logout/', views.logoutUser, name = "logout"),

]


