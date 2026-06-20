from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Todo
from .serializers import TodoSerializer

class TodoListCreateAPIView(ListCreateAPIView):
    # queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class TodoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)