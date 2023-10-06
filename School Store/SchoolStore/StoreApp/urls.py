from django.urls import path
from .import views
appname= 'StoreApp'

urlpatterns = [
    path('',views.home,name='home'),
    path('index',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('store_form',views.store_form,name='store_form'),
    path('msg',views.msg,name='msg'),
]
