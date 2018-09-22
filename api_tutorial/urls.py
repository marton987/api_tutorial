"""api_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from api_tutorial import views as api_urls
from starwars import views as starwars_urls

router = routers.DefaultRouter()
router.register(r'users', api_urls.UserViewSet)
router.register(r'planets', starwars_urls.PlanetViewSet)
router.register(r'people', starwars_urls.PeopleViewSet)
router.register(r'starships', starwars_urls.StarshipViewSet)
router.register(r'vehicles', starwars_urls.VehicleViewSet)
router.register(r'species', starwars_urls.SpeciesViewSet)
router.register(r'films', starwars_urls.FilmViewSet)
router.register(r'heroes', starwars_urls.HeroViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/', include('rest_framework.urls', namespace='rest_framework'))
]
