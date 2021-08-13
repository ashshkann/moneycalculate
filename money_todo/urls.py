from django.urls import path
from .views import views_todo, creat_todo, delet_todo

urlpatterns = [
    path('todo-list/', views_todo, name='todo-list'),
    path('creat-todo/', creat_todo),
    path('delet-todo/<todoid>/', delet_todo), 
]
