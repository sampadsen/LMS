from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),

    path('student',views.student,name="student"),
    path('issue',views.issue,name="issue"),
    path('returnbook',views.returnbook,name="returnbook"),


    path('issued',views.issued,name="issued"),
]
