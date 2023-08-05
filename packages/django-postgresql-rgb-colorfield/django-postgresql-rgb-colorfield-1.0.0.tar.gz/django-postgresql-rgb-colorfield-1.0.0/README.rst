=====
Django Postgresql RGB ColorField
=====

This is a ColorField based on django's `from django.contrib.postgres.ArrayField`. Though it shows Hex in admin and let you pick color, it is saving its value as rgb array. Which is perticularly useful if you want to do query and calculation over it. e.g. Getting colors close to another.


Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'colorfield',
    ]

2. Import and Use `ColorField`::

     from django.db import models
     from .fields import ColorField
     # Create your models here.

     class ColorPallate(models.Model):
         color1 = ColorField(null=True, blank=True)
         color2 = ColorField(null=True, blank=True)
         color3 = ColorField(null=True, blank=True)
    
         def __str__(self):
             return f"Pallate {self.id}"
