from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    """Model a task."""
    title = models.CharField(max_length=100)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, editable=False
        )
    short_description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField()

    def __str__(self):
        """Return a string representation of the model."""
        return f'{self.title.lower()}'