from django.db import models
from django_extensions.db.models import TimeStampedModel
from treebeard.mp_tree import MP_Node


class Category(MP_Node, TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class RoadmapNode(MP_Node, TimeStampedModel):
    name = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, blank=True, related_name='roadmaps')

    class Meta:
        verbose_name = 'Node'
        verbose_name_plural = 'Nodes'

    def __str__(self):
        return self.name
