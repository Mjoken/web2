from django.urls import path, include
from django.contrib import admin
from .views import *

##'' значит переход при пустой страничке (первый аргумент '') переходит на этот адрес
    ##"Второй аргумент это функция для возврата реквеста"""
    ###НЕ ЗАБУДЬ В SETTING ПРОПИСАТЬ ДЛЯ МОДУЛЯ ПУТЬ В INSTALLED APPS####

urlpatterns = [
    path('', index),
    path('index.html', index),
    path('index_add.html', index_add),
    path('index_del.html', index_del),
    path('index_info.html', index_info),
    path('index_auth.html', index_auth),
]