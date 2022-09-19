=====
Catalogs
=====

Esta aplicación Django permite tener los catálogos
para los diferentes proyectos: pfm-service, core-service y saving-service
-----------

1. Agregar "catalogs" al listado de aplicaciones instaladas dentro del archivo settings.py del proyecto::

    INSTALLED_APPS = [
        ...
        'catalogs',
    ]

2. Agregar la ruta de catálogos a la configuración global de urls::

    path('catalogs/', include('catalogs.urls')),
