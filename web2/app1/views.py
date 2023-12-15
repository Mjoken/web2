from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from students.forms import CustomUserCreationForm
from .models import *


###ФУНКЦИИ ДЛЯ РЕКВЕСТОВ (СТРАНИЦЫ)###
def index(request):
    studysession = StudySession.objects.all()
    user = request.user
    return render(request, "html/index.html", {"studysession": studysession, "user": user})


def index_addDel(request):
    studysession = StudySession.objects.all()
    return render(request, "html/index_addDel.html", {"studysession": studysession})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        studysession = StudySession()
        studysession.group = request.POST.get("group")
        studysession.title = request.POST.get("title")
        studysession.short_title = request.POST.get("short_title")
        studysession.session_type = request.POST.get("session_type")
        studysession.subgroup = request.POST.get("subgroup")
        studysession.comment = request.POST.get("comment")
        studysession.time_start = request.POST.get("time_start")
        studysession.time_end = request.POST.get("time_end")
        studysession.save()
    return HttpResponseRedirect("/")


# изменение данных в бд
def edit(request, id):
    try:
        studysession = StudySession.objects.get(id=id)

        if request.method == "POST":
            studysession.group = request.POST.get("group")
            studysession.title = request.POST.get("title")
            studysession.short_title = request.POST.get("short_title")
            studysession.session_type = request.POST.get("session_type")
            studysession.subgroup = request.POST.get("subgroup")
            studysession.comment = request.POST.get("comment")
            studysession.time_start = request.POST.get("time_start")
            studysession.time_end = request.POST.get("time_end")
            studysession.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "html/edit.html", {"studysession": studysession})
    except StudySession.DoesNotExist:
        return HttpResponseNotFound("<h2>StudySession not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        studysession = StudySession.objects.get(id=id)
        studysession.delete()
        return HttpResponseRedirect("/")
    except StudySession.DoesNotExist:
        return HttpResponseNotFound("<h2>StudySession not found</h2>")


def index_info(request):
    return render(request, "html/index_info.html")


def index_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # получаем имя пользователя и пароль из формы
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            # выполняем аутентификацию
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'html/index_register.html', {'form': form})


def index_login(request):
    return render(request, "html/index_login.html")


def index_logout(request):
    logout(request)
    return redirect('/login')
