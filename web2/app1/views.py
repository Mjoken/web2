from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import StudySession

###ФУНКЦИИ ДЛЯ РЕКВЕСТОВ (СТРАНИЦЫ)###
def index(request):
    return render(request, "html/index.html")


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

def index_auth(request):
    return render(request, "html/index_auth.html")


def index_info(request):
    return render(request, "html/index_info.html")
