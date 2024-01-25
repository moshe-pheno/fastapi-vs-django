# FastAPI _vs_ Django

## Why FastAPI

- Faster
- Simpler
- More fun
- Less learning
- Cleaner code
- Editor completion and type checks
- data validation based on type hints
- openapi docs based on type hints


## Comparison

|                 | Django                                    | FastAPI                                  |
|-----------------|-------------------------------------------|------------------------------------------|
| Link            | [Website](https://www.djangoproject.com/) | [Website](https://fastapi.tiangolo.com/) |
| Initial Release | 2005                                      | 2018                                     |
| Github Stars    | 75k                                       | 67k                                      |


## Code examples

In this repository the same application is implemented in both frameworks.  

- Compare [`fastapi/api.py`](https://github.com/moshe-pheno/fastapi-vs-django/blob/main/fastapi/api.py) vs [`django/app/urls.py`](https://github.com/moshe-pheno/fastapi-vs-django/blob/main/django/app/urls.py)
- See [example pull request](https://github.com/moshe-pheno/fastapi-vs-django/pull/1) for how a simple change looks like in both frameworks.


## Problems with Django

### Type Checking

Mypy warns about wrong types in fastapi:

![image](./screenshots/mypy-fastapi.png)

But not about django serializers:

![image](./screenshots/mypy-django.png)

### Autocompletion

Pydantic models used by fastapi are recognized by editor:

![image](./screenshots/autocomplete-fastapi.png)

Django serializers are not:

![image](./screenshots/autocomplete-django.png)

### Request Signature

Request content can be type-checked in fastapi:

![image](./screenshots/request-body-fastapi.png)

But not in django:

![image](./screenshots/request-body-django.png)


### False OpenAPI Specifications

In fastapi, the OpenAPI apecifications are always the reality:

![image](./screenshots/openapi-fastapi.png)

In djano, the specs can be totally false:

![image](./screenshots/openapi-django.png)



### Django Code is Less Readable


Compare the code [`fastapi/api.py`](https://github.com/moshe-pheno/fastapi-vs-django/blob/main/fastapi/api.py) vs [`django/app/urls.py`](https://github.com/moshe-pheno/fastapi-vs-django/blob/main/django/app/urls.py) and judge for yourself.


## API Gateway + Lambda

Using FastAPI as a lambda handler is so simple, see [this pull request](https://github.com/moshe-pheno/fastapi-vs-django/pull/2).

Instead of having to read an `event` json and return a `response` json, the [Mangum](https://mangum.io/) library will correctly process the request using the existing fastapi app.

### Why do we want this?

- Let's say you planned an API that is supposed to run on ECS and you change your mind and want it to operate as a lambda. It's [literally a single line of code](https://github.com/moshe-pheno/fastapi-vs-django/pull/2).
- You get all FastAPI adventages:
    - Less code
    - Readability
    - Simplicity
    - Type checks
    - Autocompletion
    - Faster development
    - Swagger out of the box

It's also possible to use [Mangum with django](https://mangum.io/asgi-frameworks/#django) but for a lambda, django start time might be slower.


## FastAPI + Django = Django Ninga

It's worth noting that it is simple to use django as an ORM even when using FastAPI as the http server framework.

However it is also possible to use [Django Ninja](https://django-ninja.dev/) which combines the fastapi experience into the django framework.
