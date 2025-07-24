from django.views.generic import ListView, DetailView, CreateView 
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo
from .forms import TodoForm


class TodoListView(ListView):
    """List of todos."""
    model = Todo
    template_name = 'todos/todo_list.html'
    context_object_name = 'todos'


class TodoDetailView(DetailView):
    "A todo."
    model = Todo
    template_name = 'todos/todo_detail.html'


class TodoCreateView(CreateView):
    """Create a todo."""
    model = Todo
    template_name = 'todos/todo_create.html'
    fields = '__all__'
    success_url = reverse_lazy('home')


class TodoUpdateView(UpdateView):
    """Update a todo."""
    model = Todo
    template_name = 'todos/todo_update.html'
    fields = ['title', 'short_description', 'is_done']
    success_url = reverse_lazy('home')


class TodoDeleteView(DeleteView):
    """Delete a todo."""
    model = Todo
    template_name = 'todos/todo_delete.html'
    success_url = reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo'] = self.get_object()
        return context
    
