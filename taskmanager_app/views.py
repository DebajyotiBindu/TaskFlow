from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def landing(request):
    if request.user.is_authenticated:
        return redirect('task_list')
    return render(request,'landing.html')

@login_required(login_url='login')
def task_list(request):
    tasks=Task.objects.filter(user=request.user)
    priority_filter=request.GET.get('priority')
    if priority_filter:
        tasks=tasks.filter(priority_model=priority_filter)
    completed_filter=request.GET.get('completed')
    if completed_filter:
        if completed_filter=='true':
            tasks=tasks.filter(completed=True)
        elif completed_filter=='false':
            tasks=tasks.filter(completed=False)
    sort_by=request.GET.get("sort_by")
    if sort_by:
        if sort_by=='title':
            tasks=tasks.order_by('title')
        elif sort_by=='priority_model':
            tasks=tasks.order_by('priority_model')
        else:
            tasks=tasks.order_by('completed')
    due_date_filter=request.GET.get('due_date')
    if due_date_filter:
        tasks=tasks.filter(due_date=due_date_filter)
    today=timezone.localdate()
    due_status_filter=request.GET.get('due_status')
    if due_status_filter:
        if due_status_filter=='overdue':
            tasks=tasks.filter(due_date__lt=today,completed=False)
        elif due_status_filter == 'today':
            tasks = tasks.filter(due_date=today, completed=False)

        elif due_status_filter == 'upcoming':
            tasks = tasks.filter(due_date__gt=today, completed=False)

        elif due_status_filter == 'none':
            tasks = tasks.filter(due_date__isnull=True)
    for task in tasks:
        if(task.due_date and task.due_date<today and not task.completed):
            task.overdue=True
    return render(request,'task_list.html',{'tasks':tasks,'due_date_filter':due_date_filter})

@login_required(login_url='login')
def add_task(request):
    error=None
    if request.method=='POST':
        task_name=request.POST.get('title','').strip()
        if not task_name:
            error="Task name cannot be empty"
        else:
            description=request.POST.get('description','').strip()
            completed=request.POST.get('completed')=='on'
            priority=request.POST.get('priority')
            valid_priorities=[choice[0] for choice in Task.PRIORITY_CHOICES]
            if priority not in valid_priorities:
                priority="Medium"
            due_date=request.POST.get('due_date')
            if task_name:
                Task.objects.create(
                    title=task_name,
                    description=description,
                    completed=completed,
                    priority_model=priority,
                    due_date=due_date if due_date else None,
                    user=request.user
                )
                messages.success(request, 'Task added successfully.')
                return redirect('task_list')

    return render(request,'add_task.html',{'error':error})

@login_required(login_url='login')
def edit_task(request,id):
    task=get_object_or_404(Task,id=id,user=request.user)
    if request.method=='POST':
        task_name=request.POST.get("title")
        description=request.POST.get("description")
        completed=request.POST.get("completed")=="on"
        priority=request.POST.get("priority")
        due_date=request.POST.get("due_date")
        task.due_date=due_date if due_date else None
        task.title=task_name
        task.description=description
        task.completed=completed
        task.priority_model=priority
        task.save()
        messages.success(request, 'Task updated successfully.')
        return redirect('task_list')

    return render(request,'edit_task.html',{'task':task})

@login_required(login_url='login')
def delete_task(request,id):
    task=get_object_or_404(Task,id=id,user=request.user)
    if request.method=='POST':
        task.delete()
        messages.success(request, 'Task deleted successfully.')
        return redirect('task_list')

    return render(request,'delete_task.html',{'task':task})

def signup(request):
    if request.method=='POST':
        email=request.POST.get("email")
        password=request.POST.get("password")
        if User.objects.filter(email=email).exists():
            return render(
                request,
                "signup.html",
                {"error":"User already exists"}
            )
        u=User.objects.create_user(username=email,email=email,password=password)
        u.save()
        return redirect('login')
    return render(request,"signup.html")

def login(request):
    if request.method=='POST':
        email=request.POST.get("email")
        password=request.POST.get("password")

        user=authenticate(request,username=email,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('task_list')
        return render(request,'login.html',{'error':'Invalid email or password'})
    return render(request,"login.html")

@login_required(login_url='login')
def logout(request):
    if request.method=='POST':
        auth_logout(request)
        return redirect('login')