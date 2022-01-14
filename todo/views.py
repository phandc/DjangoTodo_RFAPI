from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import TodoSerialier
from .models import Todo
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters #enable ?search
from .pagination import CustomPageNumberPagination

class TodoAPIView(ListCreateAPIView):
    serializer_class = TodoSerialier
    permisson_classes = (IsAuthenticated,)
    pagination_class = CustomPageNumberPagination # custom pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['id','title', 'is_complete'] # Sepicify which fileds can be filtered: synstax ?field=""
    search_fields = ['id','title', 'is_complete']
    ordering_fields = ['id','title', 'is_complete']

    def perform_create(self, serializer): #consider
            return serializer.save(owner=self.request.user)   

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerialier
    permisson_classes = (IsAuthenticated,)
    lookup_field = "id" #search by id

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

# class CreateTodoAPIView(CreateAPIView):
#     serializer_class = TodoSerialier
#     permisson_classes = (IsAuthenticated,)

#     def perform_create(self, serializer): #consider
#             return serializer.save(owner=self.request.user)


# class TodoListAPIView(ListAPIView):
#     serializer_class = TodoSerialier
#     permisson_classes = (IsAuthenticated,)
#     # querySet = Todo.objects.all()

#     def get_queryset(self):
#         return Todo.objects.filter(owner=self.request.user)