

from django.contrib import admin
from django.urls import path , include

from django.conf import settings
from django.conf.urls.static import static

from . import views 


app_name = "blog"
urlpatterns = [
    
    path('', views.home),
    path('articles/', views.home , name = "home"),
    path('articles/<slug:slug>', views.detail_article , name = "detail"),
    path('category/<slug:slug>', views.category , name = "category"),

]