from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    return render(request, "tasks/index.html", {"tasks": tasks})

def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks_index")
    else:
        form = TaskForm()
    return render(request, "tasks/create.html", {"form": form})

def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks_index")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/update.html", {"form": form})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect("tasks_index")
    return render(request, "tasks/delete.html", {"task": task})
