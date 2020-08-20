from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import ToDoList



def home(request):
    context = {
        'todos': ToDoList.objects.all(),
        'title' :'home'
        }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = ToDoList
    template_name = 'blog/home.html'
    context_object_name = 'todos'

class ToDoListCreateView(CreateView):
    success_url = '/'
    model = ToDoList
    fields = ['todo', 'desc']
    success_url = '/'

class ToDoListUpdateView(UpdateView):
    model = ToDoList
    fields = ['todo', 'desc']
    success_url = '/'
    
class ToDoListDeleteView(DeleteView):
    model = ToDoList
    success_url = '/'

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

def todo(request):
    return render(request, 'blog/todo.html', {'title':'TO-DO'})
