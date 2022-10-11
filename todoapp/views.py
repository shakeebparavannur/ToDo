import re
from django.shortcuts import redirect, render , get_object_or_404
from .models import Task
from django.views.generic import ListView,DetailView,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def task_add(request):
    if request.method=='POST':
        name=request.POST.get('task')
        details=request.POST.get('details')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        task=Task(name=name,date=date,priority=priority,details=details,user=request.user)
        task.save()

    task_list=Task.objects.filter(user=request.user).order_by('-date')

    return render(request,'index.html',{'task':task_list})

class TaskListView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task'

class DeleteListView(DeleteView):
    model = Task
    success_url = reverse_lazy('home')
    template_name = 'delete.html'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'

UserModel = get_user_model

class TaskUpdateView(UpdateView):
    model = Task
    fields = [
        "name",
        "date",
        "priority",
        "details",
    ]
    template_name = 'update.html'
    context_object_name = 'task'
    success_url = reverse_lazy('home')


def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
                return redirect('/')
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Email already in use")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('/')
        else:
            messages.warning(request,"password not match")
            return redirect('reg')
        return redirect('')

    return render(request,'reg.html')


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('login')
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


class TaskListView1(ListView):
    model = Task
    template_name = 'list.html'
    context_object_name = 'task'
    
