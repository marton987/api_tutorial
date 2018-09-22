from rest_framework import serializers

from starwars.models import Film, Species, Starship, People, Planet, Hero, Vehicle


class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = (
            'name', 'rotation_period', 'orbital_period', 'diameter',
            'climate', 'gravity', 'terrain', 'surface_water', 'population',
        )


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = (
            'name', 'height', 'mass', 'hair_color', 'skin_color',
            'eye_color', 'birth_year', 'gender', 'homeworld',
        )


class StarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Starship
        fields = (
            'name',  'model', 'manufacturer', 'cost_in_credits', 'length',
            'max_atmosphering_speed', 'crew', 'passengers', 'cargo_capacity',
            'consumables', 'hyperdrive_rating', 'MGLT', 'starship_class',
            'pilots',
        )


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = (
            'name',  'model', 'manufacturer', 'cost_in_credits', 'length',
            'max_atmosphering_speed', 'crew', 'passengers', 'cargo_capacity',
            'consumables', 'vehicle_class', 'pilots'
        )


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = (
            'name', 'classification', 'designation', 'average_height',
            'skin_colors', 'hair_colors', 'eye_colors', 'average_lifespan',
            'homeworld', 'language', 'people',
        )


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = (
            'title', 'episode_id', 'opening_crawl', 'director', 'producer',
            'release_date', 'characters', 'planets', 'starships', 'vehicles',
            'species'
        )


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'homeworld')
