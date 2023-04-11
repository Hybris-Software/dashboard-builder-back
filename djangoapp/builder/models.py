from django.db import models

# Create your models here.

# Create a choices for layout types


class LayoutType(models.TextChoices):
    BASE = 'base'
    DASHBOARD = 'dashboard'


class Layout(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    structure = models.JSONField()
    layout_type = models.CharField(
        max_length=50, choices=LayoutType.choices, default=LayoutType.BASE)

    def __str__(self):
        return self.name
