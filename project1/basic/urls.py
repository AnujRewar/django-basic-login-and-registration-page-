from django.contrib import admin
from django.urls import path
from basic import views
urlpatterns=[
    path('',views.index,name='index'),
    path('register/',views.register,name="register")
]