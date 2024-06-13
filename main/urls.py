from unicodedata import name
from django.urls import path ,include
from .views import *
from django.contrib.auth.views import LogoutView
app_name='main'



urlpatterns = [
    # path('<int:pk>/',TaskDetail.as_view(),name='detail_list'),
    # path('create-task',TaskCreate.as_view(),name='create_task'),
    # path('update-task/<int:pk>/',TaskUpdate.as_view(),name='task_update'),
    # # path('delete-task/<int:pk>/',TaskDelete.as_view(),name='task_delete'),
    # path('delete-task/<int:pk>/',TaskDelete,name='task_delete'),
    path('dashboard/<str:slug>/',home,name='home'),
    path('',exam,name='exam'),
    path('create-quick',ExamCreatequick.as_view(),name='ExamCreatequicks'),
    path('create-quick/update/<int:pk>/',Examupdatequick.as_view(),name='Examupdatequicks'),
    path('create-Full/update/<int:pk>/',ExamupdateFull.as_view(),name='ExamupdateFulls'),
    path('create-full',ExamCreateFull.as_view(),name='ExamCreateFulls'),
    
    
    
    
    path('examquick/<int:pk>/',examquick,name='examquick'),
    path('examfull/<int:pk>/',examfull,name='examfull'),
    path('save-answer/', SaveAnswerView.as_view(), name='save-answer'),
]
