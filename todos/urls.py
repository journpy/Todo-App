from django.urls import path
from .views import TodoListView, TodoDetailView, TodoCreateView


urlpatterns = [
    path('', TodoListView.as_view(), name='home'),
    path('<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('create/', TodoCreateView.as_view(), name='todo-create'),
]