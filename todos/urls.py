from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_todos, name='user_todos'),  
    path('<int:id>/', views.user_todo_detail, name='user_todo_detail'),  
    path('create/', views.create_todo, name='create_todo'), 
    path('<int:id>/delete/', views.delete_todo, name='delete_todo'),  
]
