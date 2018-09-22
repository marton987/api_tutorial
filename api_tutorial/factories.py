import factory
from django.contrib.auth.models import User


class UserFactory(factory.DjangoModelFactory):
    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    password = 'password'

    class Meta:
        model = User
