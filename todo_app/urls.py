from django.urls import path

from .views import (
    todo_list_create,
    todo_retrieve_update_destroy,
    TodoListCreateAPIView,
    TodoRetrieveUpdateDestroyAPIView


)

urlpatterns = [
    # path("todos/", todo_list_create),
    # path("todo/<int:pk>", todo_retrieve_update_destroy),

    path("todos/", TodoListCreateAPIView.as_view()),
    path("todo/<int:pk>", TodoRetrieveUpdateDestroyAPIView.as_view()),
]
