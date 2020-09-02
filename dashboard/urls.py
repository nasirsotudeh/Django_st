from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
   
   path('',  views.index, name = 'index'),
   path('index' , views.index, name = 'index'),

   path('accounts/login/', views.login_view),
   path('register/', views.register_view),
   path('accounts/logout/', views.logout_view)

]
