"""
URL configuration for config project.

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
<<<<<<< HEAD
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    ]
=======

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.APIs")),
]
>>>>>>> 06e448c8eb44488c023b984a1bf6014e8c6ab661
