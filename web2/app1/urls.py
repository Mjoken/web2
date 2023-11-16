from django.urls import path, include
from django.contrib import admin
from .views import *

urlpatterns = [
    path('', app1), ##'' значит переход при пустой страничке (первый аргумент '') переходит на этот адрес
    ##"Второй аргумент это функция для возврата реквеста"""
    ###НЕ ЗАБУДЬ В SETTING ПРОПИСАТЬ ДЛЯ МОДУЛЯ ПУТЬ В INSTALLED APPS####
]