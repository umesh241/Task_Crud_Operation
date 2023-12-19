from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as loginUser, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def home(req):
    if req.user.is_authenticated:
        user = req.user 
        form = TaskForm()
        Tasks = Task.objects.filter(user=user)
        return render(req, 'index.html', {'form': form, 'Tasks': Tasks})


def login(req):
    if req.method == 'GET':
        form1 = AuthenticationForm()
        return render(req, 'login.html', {"form": form1})
    else:
        form = AuthenticationForm(data=req.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                loginUser(req, user)
                return redirect('home')
        else:
            return render(req, 'login.html', {"form": form})


def signup(req):
    if req.method == 'GET':
        form = UserCreationForm()
        return render(req, 'signup.html', {"form": form})
    else:
        # print(req.POST)
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('/login/')
        else:
            return render(req, 'signup.html', {"form": form})


@login_required(login_url='login')
def add_Task(req):
    if req.user.is_authenticated:
        user = req.user
        print(user)
        form = TaskForm(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Task = form.save(commit=False)
            Task.user = user
            Task.save()
            print(Task)
            return redirect("home")
        else:
            return render(req, 'index.html', {'form': form})


def delete_Task(req, id):
    Task.objects.get(pk=id).delete()
    return redirect('home')


def change_Task(req, id, status):
    Task1 = Task.objects.get(pk=id)
    Task1.status = status
    Task1.save()
    return redirect('home')


def signout(req):
    logout(req)
    return redirect('login')


@api_view(['GET'])
def listTask(req):
    td = Task.objects.all()
    serializer = TaskSerializer(td, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def listTaskDetail(req, pk):
    td = Task.objects.get(id=pk)
    serializer = TaskSerializer(td, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def Task_delete(req, pk):
    td = Task.objects.get(id=pk).delete()
    serializer = TaskSerializer(td, many=False)
    return Response(serializer.data)
