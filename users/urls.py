from unicodedata import name
from django.urls import path ,include
from .views import *
from django.contrib.auth.views import LogoutView
app_name='users'



urlpatterns = [
    # path('',TaskList.as_view(),name='task_list'),
    # path('<int:pk>/',TaskDetail.as_view(),name='detail_list'),
    # path('create-task',TaskCreate.as_view(),name='create_task'),
    # path('update-task/<int:pk>/',TaskUpdate.as_view(),name='task_update'),
    # # path('delete-task/<int:pk>/',TaskDelete.as_view(),name='task_delete'),
    # path('delete-task/<int:pk>/',TaskDelete,name='task_delete'),
    path('accounts/login',Login.as_view(),name='login'),
    path('accounts/register',Regiser.as_view(),name='register'),
    path('logout',LogoutView.as_view(next_page='todo_list:login'),name='logout'),
    

]
