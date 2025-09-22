from django.urls import path
from django.contrib import admin
from . import views

app_name = 'basic_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/',views.user_login, name='login' ),
    path('logout', views.user_logout, name='logout'),
    path('tasks', views.TaskListView.as_view(), name='task_list'),
    path('delete/<int:pk>', views.DeleteTaskView.as_view(), name='delete'),
    path('addtask/',views.TaskCreateView.as_view(), name='addtask'),
    path('updatetask/<int:pk>',views.TaskUpdateView.as_view(), name='updatetask'),
    
]

