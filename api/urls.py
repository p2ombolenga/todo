from django.urls import path
from .views import TodoListCreateAPIView, TodoRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('todo/', TodoListCreateAPIView.as_view()),
    path('todo/<int:pk>/', TodoRetrieveUpdateDestroyAPIView.as_view()),
]
