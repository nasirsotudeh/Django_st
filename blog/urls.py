

from django.contrib import admin
from django.urls import path , include

from django.conf import settings
from django.conf.urls.static import static

from . import views 
from .views import Articlelist , ArticleDetail , CategoryList

app_name = "blog"
urlpatterns = [
    
    path('', Articlelist.as_view(), name="first"),
    path('articles/', Articlelist.as_view() , name = "home"),
    path('articles/<slug:slug>', ArticleDetail.as_view() , name = "detail"),
    path('category/<slug:slug>', CategoryList.as_view() , name = "category"),

]