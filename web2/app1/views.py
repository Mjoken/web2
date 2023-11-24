from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import StudySession

###ФУНКЦИИ ДЛЯ РЕКВЕСТОВ (СТРАНИЦЫ)###
def index(request):
    return render(request, "html/index.html")


def index_addDel(request):
    studySession = StudySession.objects.all()
    return render(request, "html/index_addDel.html")

# сохранение данных в бд
def create(request):
    if request.method == "POST":
        studySession = StudySession()
        studySession.group = request.POST.get("group")
        studySession.title = request.POST.get("title")
        studySession.short_title = request.POST.get("short_title")
        studySession.session_type = request.POST.get("session_type")
        studySession.subgroup = request.POST.get("subgroup")
        studySession.comment = request.POST.get("comment")
        studySession.time_start = request.POST.get("time_start")
        studySession.time_end = request.POST.get("time_end")
        studySession.save()
    return HttpResponseRedirect("/")


# изменение данных в бд
def edit(request, id):
    try:
        studySession = StudySession.objects.get(id=id)

        if request.method == "POST":
            studySession.group = request.POST.get("group")
            studySession.title = request.POST.get("title")
            studySession.short_title = request.POST.get("short_title")
            studySession.session_type = request.POST.get("session_type")
            studySession.subgroup = request.POST.get("subgroup")
            studySession.comment = request.POST.get("comment")
            studySession.time_start = request.POST.get("time_start")
            studySession.time_end = request.POST.get("time_end")
            studySession.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"studySession": studySession})
    except StudySession.DoesNotExist:
        return HttpResponseNotFound("<h2>StudySession not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        studySession = StudySession.objects.get(id=id)
        studySession.delete()
        return HttpResponseRedirect("/")
    except StudySession.DoesNotExist:
        return HttpResponseNotFound("<h2>StudySession not found</h2>")

def index_auth(request):
    return render(request, "html/index_auth.html")


def index_info(request):
    return render(request, "html/index_info.html")
