# Django-Ubigeo-Peru

django-ubigeo-peru, es una app que te permitira implementar facilmente los ubigeos de Perú, en tus django app.
## Notice
En este fork he cambiado el modelo para que no dependa el código del ubigeo puesto a que este es variante el tiempo.


# Instalar

En tu settings.py

```python
    INSTALLED_APPS = (
        ....
        'ubigeo',
    )
```


En tu urls.py

```python
    urlpatterns = patterns('',
        ....
        (r'^ubigeo/', include('ubigeo.urls')),
    )
```

# TODO
- Refactor Javascript functions to recieve a selector as an argument in the example aplication.

# Licencia
ver LICENSE
