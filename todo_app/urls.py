from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    todo_list_create,
    todo_retrieve_update_destroy,
    TodoListCreateAPIView,
    TodoRetrieveUpdateDestroyAPIView,
    TodoModelViewSet
)


router = DefaultRouter()
router.register("todo", TodoModelViewSet)

urlpatterns = [
    # path("todos/", todo_list_create),
    # path("todo/<int:pk>", todo_retrieve_update_destroy),

    # path("todos/", TodoListCreateAPIView.as_view()),
    # path("todo/<int:pk>", TodoRetrieveUpdateDestroyAPIView.as_view()),

    path("", include(router.urls))
]
