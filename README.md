# API Tutorial

This is a Django Tutorial that contains a example with REST API and GraphQL.

## References

The data for the tutorial is obtained from https://github.com/graphql-python/swapi-graphene

## Configuration

Please follow these steps:

1. Clone the [repository](https://github.com/marton987/api_tutorial)

1. Checkout the branch depending of your need for the tutorial

    - [REST](https://github.com/marton987/api_tutorial/tree/rest)
    - [GraphQL](https://github.com/marton987/api_tutorial/tree/graphql)

1. Install [pip](https://pip.pypa.io/en/latest/installing.html) and
[virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)

1. Install project dependencies

        $ pip install -r requirements.txt
        
1. Run docker-compose

        $ docker-compose up
        
1. Initialize your database

        $ python manage.py migrate

1. Create superuser account

        $ python manage.py createsuperuser

1. Run your server

        $ python manage.py runserver 0.0.0.0:8000

1. Run your tests

        $ python manage.py test
