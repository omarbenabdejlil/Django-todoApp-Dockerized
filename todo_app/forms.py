from django import forms
from django.forms import ModelForm
from todo_app.models import Task
"""
class Task(models.Model):
    title = models.CharField(max_length=500)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
"""


class AddTaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))

    class Meta:
        model = Task
        fields = '__all__'


