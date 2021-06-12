# syntax almost same as syntax in urls.py in first_project
from django.urls import path
from . import views  # from current directory import views

urlpatterns = [
    path('', views.myfunctioncall, name="index"),  # url name is index
    # request to the about page
    path('about', views.myfuncabout, name="about"),
    path('add/<int:a>/<int:b>', views.add, name="add"),
    path('intro/<str:name>/<int:age>', views.intro, name="intro"),
    path('myfirstpage', views.myfirstpage, name='myfirstpage'),
    path('mysecondpage', views.mysecondpage, name='mysecondpage'),
    path('mythirdpage', views.mythirdpage, name='mythirdpage'),
    path("myimagepage", views.myimagepage, name="myimagepage"),
    path("myimagepage2", views.myimagepage2, name="myimagepage2"),
    path("myimagepage3/<str:imagename>", views.myimagepage3, name="myimagepage3"),
    path("myformpage", views.myformpage, name="myformpage"),
    path("submitmyform", views.submitmyform, name="submitmyform"),  
    path("myform2", views.myform2, name="myform2"),
]
