from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import TodoForm
from .models import Todo

@login_required
def user_todos(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todos/user_todos.html', {'todos': todos})

@login_required
def user_todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    return render(request, 'todos/todo_detail.html', {'todo': todo})

@login_required
def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('user_todos')
    else:
        form = TodoForm()
    return render(request, 'todos/create_todo.html', {'form': form})

@login_required
def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('user_todos')
    return render(request, 'todos/delete_confirm.html', {'todo': todo})
