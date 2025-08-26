from django.urls import path

from todo_app import views

urlpatterns = [  
    path("", views.todo_list, name="todo-list"),
    path("remove/<int:id>/", views.todo_delete, name="todo-delete"),
    path("add/", views.todo_create, name="todo-create"),          # routing or path
    path("edit/<int:id>/", views.todo_update, name="todo-update"),
]