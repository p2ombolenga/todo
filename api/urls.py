from django.urls import path
from .views import TodoListCreateAPIView, TodoRetrieveUpdateDestroyAPIView, RootAPIView

urlpatterns = [
    path('', RootAPIView.as_view(), name='root'),
    path('todo/', TodoListCreateAPIView.as_view(), name='todos'),
    path('todo/<int:pk>/', TodoRetrieveUpdateDestroyAPIView.as_view()),
]
