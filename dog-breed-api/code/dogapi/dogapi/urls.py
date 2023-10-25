# @Author: Matthew Hale <mlhale>
# @Date:   2023-09-11T18:14:37-05:00
# @Email:  mlhale@unomaha.edu
# @Filename: urls.py
# @Last modified by:   mlhale
# @Last modified time: 2023-09-18T18:30:03-05:00
# @Copyright: Copyright (C) 2019 Matthew L. Hale



"""
URL configuration for dogapi project.

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
from dogs import views
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'dogs', views.DogDBViewSet)
#router.register(r'dogs/<int:pk>', views.DogDBViewSet)
router.register(r'breeds', views.BreedDBViewSet)
#router.register(r'breeds/<int:pk>', views.BreedDBViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
