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
import re

from django.conf import settings
from django.conf.urls import url
from django.views.static import serve
from django.contrib import admin
from django.urls import path

from graphene_django.views import GraphQLView

from graphql import GraphQLCoreBackend


# Hack for allow static files in prod (Heroku/Dokku)
def static(prefix, view=serve, **kwargs):
    return [
        url(r'^%s(?P<path>.*)$' % re.escape(prefix.lstrip('/')), view, kwargs=kwargs),
    ]


urlpatterns = [
    path('admin/', admin.site.urls),
    # url('', include('starwars.urls')),
    url(r'^graphql', GraphQLView.as_view(graphiql=True, backend=GraphQLCoreBackend())),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
