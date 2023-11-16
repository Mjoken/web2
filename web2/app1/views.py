from django.shortcuts import render

###ФУНКЦИИ ДЛЯ РЕКВЕСТОВ (СТРАНИЦЫ)###
def index(request):
    return render(request, "html/index.html")
def index_add(request):
    return render(request, "html/index_add.html")
