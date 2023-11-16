from django.shortcuts import render

###ФУНКЦИИ ДЛЯ РЕКВЕСТОВ (СТРАНИЦЫ)###
def app1(request):
    return render(request, "app1/app1.html")
