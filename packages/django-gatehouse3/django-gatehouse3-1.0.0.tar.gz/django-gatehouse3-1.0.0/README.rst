=====
Gatehouse3
For Django 2.0 and Python3
=====

This is a simple Django application that allows you to add guests and visits.
Visits are visible to the people working in the gatehouse.
The app also helps the catering staff


Quick start
-----------
1. Install Django Gatehouse

    pip install django-gatehouse3

2. Add "gatehouseapp" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'gatehouseapp',
    ]

3. Include the gatehouse URLconf in your project urls.py like this::

    path(r'', include('gatehouseapp.urls')),

4. Run `python manage.py migrate` to create the gatehouse models.

