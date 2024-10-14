from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    todo_list = Todo.objects.all()
    context = {
        'todo_list': todo_list
    }
    return render(request, 'todos/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm()
    context = {
        'form': form
    }
    return render(request, 'todos/create.html', context)
    
def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)

@login_required
def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.user == todo.user:
        if request.method == 'POST':
            todo.delete()
            return redirect('todos:index')
    return redirect('todos:detail', todo.pk)

@login_required
def update(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.user == todo.user:
        if request.method == 'POST':
            form = TodoForm(request.POST, instance=todo)
            if form.is_valid():
                todo = form.save()
        else:
            form = TodoForm(instance=todo)
        context = {
            'todo': todo,
            'form': form
        }
        return render(request, 'todos/update.html', context)
    return redirect('todos:detail', todo.pk)

def my_page(request):
    todo_list = request.user.todo_set.all()
    context = {
        'todo_list': todo_list
    }
    return render(request, 'todos/my_page.html', context)