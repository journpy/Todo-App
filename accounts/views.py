from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class SignUpView(CreateView):
    """Register a user."""
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')