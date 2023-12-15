"""
URL configuration for web2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from app1 import views
from students.forms import UserLoginForm, UserCreationForm, CustomUserCreationForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
    path('/', include('app1.urls')),
    path('login/',
         auth_views.LoginView.as_view
         (template_name='html/index_login.html',
          authentication_form=UserLoginForm),
         name='login'),
    path('register/',
         views.index_register,
         name='register'),

    # стандартный вариант path('', include('имя_модуля.файл_URLS'))
    # Модуль создается через команду manage.py startapp <имя_модуля>
]
