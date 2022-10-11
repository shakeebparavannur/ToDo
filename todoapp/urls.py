from . import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns =[
    path('',views.task_add,name='home'),
    path('cbvhome/',views.TaskListView.as_view(),name='cbvhome'),
    path('delete/<pk>',views.DeleteListView.as_view(),name='cbvdelete'),
    path('details/<pk>',views.TaskDetailView.as_view(),name='cbvdetail'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout',views.logout,name='logout'),
    path('reg',views.register,name='reg'),
    path('update/<pk>',views.TaskUpdateView.as_view(),name='cbvupdate'),
    path('listview',views.TaskListView1.as_view(),name='cbvlist')
]