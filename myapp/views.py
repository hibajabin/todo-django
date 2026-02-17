from django.shortcuts import render, redirect
from .models import task
from .forms import TaskForm

def index(request):
    tasks = task.objects.all().order_by('-created')
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'myapp/index.html', {
        'tasks': tasks,
        'form': form
    })

def complete_task(request, pk):
    tasks = task.objects.get(id=pk)
    tasks.completed = True
    tasks.save()
    return redirect('index')

def delete_task(request, pk):
    tasks = task.objects.get(id=pk)
    tasks.delete()
    return redirect('index')
