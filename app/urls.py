from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('add/',views.newr,name='newr'),
    path('editu/<int:pk>/',views.editu,name='editust'),
    path('user/',views.user,name='user-page'),
    path('delete-user/<int:pk>',views.delete,name='delete-user'),
    path('update/',views.update_user,name='update')
]