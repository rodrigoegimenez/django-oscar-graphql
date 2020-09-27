# Django Oscar GraphQl

This package provides a GraphQl API for [django_oscar](https://github.com/django-oscar/django-oscar).

## Usage

1. Install the `django-oscar-graphql` package.
2. Add `graphene_django` and `oscar_graphql` to `INSTALLED_APPS`
```python
INSTALLED_APPS = [
    ...
    'graphene_django',
    'oscar_graphql',
]
```
3. Add `graphql` url to your urlconf.
```python
from django.urls import include
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = (
    # all the things you already have
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
)
```