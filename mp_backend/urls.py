"""mp_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
import mp_app.views as mp
import mp_app.util.DebugUtil as debug

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path('test/', include([
        path('json/', debug.testJson),
        path('http/', debug.testHttp),
    ])),
    path('mp/', include([
        path('', mp.index),
        path('user/<int:userId>', mp.getUserInfoByUserId),
        path('music/', mp.getAllMusic)
    ]))
]