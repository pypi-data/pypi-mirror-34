# Dynamic Upload Image Field

## Description

A django ImageField that generates it's upload_to value from the model instance method get\_upload\_to.

## Installation

```python
pip install dynamic-upload-image-field
```

or

```python
pipenv install dynamic-upload-image-field
```

## Usage

```python
from django.db import models
from dynamic_upload_image_field.fields import DynamicUploadImageField

class ExampleModel(models.Model):
    name = models.CharField(max_length=56)
    image = DynamicUploadImageField()

    def get_upload_to(self, field_name):
        class_name = self.__class__.__name__.lower()
        instance_name = self.name
        return "{}/{}".format(class_name, instance_name)
```