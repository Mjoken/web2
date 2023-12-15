from django.urls import path
from .views import *

##'' значит переход при пустой страничке (первый аргумент '') переходит на этот адрес
    ##"Второй аргумент это функция для возврата реквеста"""
    ###НЕ ЗАБУДЬ В SETTING ПРОПИСАТЬ ДЛЯ МОДУЛЯ ПУТЬ В INSTALLED APPS####

urlpatterns = [
    path('', index),
    path('index.html', index),
    path('index_addDel.html', index_addDel),
    path("create/", create),
    path("edit/<int:id>/", edit),
    path("delete/<int:id>/", delete),
    path('index_info.html', index_info),
    path('index_register.html', index_register),
    path('index_login.html', index_login),
    path('logout/', index_logout, name='logout'),
]