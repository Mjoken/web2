from django.shortcuts import render


###ФУНКЦИИ ДЛЯ РЕКВЕСТОВ (СТРАНИЦЫ)###
def index(request):
    return render(request, "html/index.html")


def index_add(request):
    return render(request, "html/index_add.html")


def index_del(request):
    return render(request, "html/index_del.html")


def index_auth(request):
    return render(request, "html/index_auth.html")


def index_info(request):
    return render(request, "html/index_info.html")
