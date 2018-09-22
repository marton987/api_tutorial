from rest_framework import viewsets, permissions

from starwars.models import Hero, Film, Species, Vehicle, Starship, People, Planet
from starwars.serializers import HeroSerializer, FilmSerializer, SpeciesSerializer, VehicleSerializer,\
    PeopleSerializer, StarshipSerializer, PlanetSerializer


class PlanetViewSet(viewsets.ModelViewSet):
    serializer_class = PlanetSerializer
    queryset = Planet.objects.all()
    permission_classes = (permissions.AllowAny,)


class PeopleViewSet(viewsets.ModelViewSet):
    serializer_class = PeopleSerializer
    queryset = People.objects.all()
    permission_classes = (permissions.AllowAny,)


class StarshipViewSet(viewsets.ModelViewSet):
    serializer_class = StarshipSerializer
    queryset = Starship.objects.all()
    permission_classes = (permissions.AllowAny,)


class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    permission_classes = (permissions.AllowAny,)


class SpeciesViewSet(viewsets.ModelViewSet):
    serializer_class = SpeciesSerializer
    queryset = Species.objects.all()
    permission_classes = (permissions.AllowAny,)


class FilmViewSet(viewsets.ModelViewSet):
    serializer_class = FilmSerializer
    queryset = Film.objects.all()
    permission_classes = (permissions.AllowAny,)


class HeroViewSet(viewsets.ModelViewSet):
    serializer_class = HeroSerializer
    queryset = Hero.objects.all()
    permission_classes = (permissions.AllowAny,)
