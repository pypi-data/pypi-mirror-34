# Django Auto ModelAdmin

## Description

Automatically creates a ModelAdmin for each model instance passed in a list. Will also create an inline model for each related model.

## Installation

```python
pip install django-auto-modeladmin
```

or

```python
pipenv install django-auto-modeladmin
```

## Methods

1. autoregister([ModelInstance/(ModelInstance, {options})]) -  Allows for a tuple to be passed instead of a model instance, to allow for extra admin options like list\_display, readonly\_fields, etc.

## Options

1. list_display - A list of field names to use as the list\_display.
2. readonly_fields - A list of field names that should be read-only.
3. exclude - A list of field names to exclude from the ModelAdmin.
4. property_fields - A list of property names on the model that should be included.

## Usage

```python
from django_auto_modeladmin import autoregister
from . import models

autoregister([
    (models.ModelName, {
        "list_display": ["id", "name"],
        "readonly_fields": ["id", "created_on", "modified_on"],
        "exclude": ["uuid"],
        "property_fields": ["full_name"],
    })
])
```