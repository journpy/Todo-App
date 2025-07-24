from django.urls import path
from .views import (
    TodoListView, 
    TodoDetailView, 
    TodoCreateView, 
    TodoUpdateView,
    TodoDeleteView,
)


urlpatterns = [
    path('', TodoListView.as_view(), name='home'),
    path('<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('create/', TodoCreateView.as_view(), name='todo-create'),
    path('update/<int:pk>/', TodoUpdateView.as_view(), name='todo-update'),
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name='todo-delete'),
]