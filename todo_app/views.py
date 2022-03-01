from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *


# Create your views here.
def index(request):
    tasks = Task.objects.all()

    form = AddTaskForm()
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'index.html', {'tasks': tasks, 'form': form})


def update(request, pk):
    task = Task.objects.get(id=pk)

    form = AddTaskForm(instance=task)
    if request.method == 'POST':
        form = AddTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'update.html', {'form': form})


def delete(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    return render(request, 'delete.html', {'item': item})
