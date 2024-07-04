from django.urls import path

from .views import todo_list_create, todo_retrieve_update_destroy

urlpatterns = [
    path("todos/", todo_list_create),
    path("todo/<int:pk>", todo_retrieve_update_destroy),
]