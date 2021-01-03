from django.db.models.signals import post_save
from django.dispatch import receiver

from roadmaps.models import RoadmapNode
from roadmaps.services.progress import ProgressPropagator


@receiver(post_save, sender=RoadmapNode)
def propagate_completion_to_descendant_nodes(sender, **kwargs):
    roadmap: RoadmapNode = kwargs.get('instance')
    ProgressPropagator.propagate_completion_desc(roadmap)
