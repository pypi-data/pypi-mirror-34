# IS Django Utils

Django Utils is a collection of utils for Django.

## Quick start

1. Add "django-utils" to your INSTALLED_APPS setting like this:

```
    INSTALLED_APPS = [
        ...
        'django_utils',
        ...
    ]
```

## AdminWithSelectRelated

- Usage:

```
    from django_utils.admin import AdminWithSelectRelated
    
    class AlumnoAdmin(AdminWithSelectRelated):
        list_display = ('estudiante', 'seccion', 'anio_lectivo', )
        list_filter = (
            ('seccion', SeccionFilter),
            'seccion__grado__anio_lectivo',
        )
        inlines = (AlumnoServicioInlineAdmin, AlumnoItemInlineAdmin, )

        list_select_related = ('estudiante__profile', 'seccion__grado__anio_lectivo', )
```

## AdminInlineWithSelectRelated

- Usage:

```
    from django_utils.admin import AdminInlineWithSelectRelated
    
    class AlumnoItemInlineAdmin(AdminInlineWithSelectRelated):
        model = AlumnoItem

        list_select_related = ('alumno__estudiante__profile', 'item__anio_lectivo', )
```

## FilterWithSelectRelated

```
    from django_utils.admin import FilterWithSelectRelated
    
    class SeccionFilter(FilterWithSelectRelated):
        list_select_related = ('grado', )
```
