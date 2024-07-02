"""
URL configuration for pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index1_view, name = 'index1'),
    path('index2/<int:id>/',views.index2_view, name='index2'),
    path('index3/',views.index3_view, name='index3'),
    path('update/<int:id>/',views.update_view, name='update'),
    path('delect/<int:id>/',views.delect_view, name='delect'),
    path('dropdown/<int:Standard>',views.drop_down_view, name='dropdown')
]
