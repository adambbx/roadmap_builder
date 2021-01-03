from unittest import mock

from django.db.models.signals import post_save
from django.test import TestCase

from roadmaps.models import RoadmapNode
from roadmaps.services.progress import ProgressPropagator


class SignalListenersModuleTestCase(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.root_node = RoadmapNode.add_root(name='Introduction to Linear Algebra')

    @mock.patch.object(ProgressPropagator, 'propagate_completion_desc')
    def test_propagate_completion_to_descendant_nodes(self, propagate_mock):
        post_save.send(sender=RoadmapNode, instance=self.root_node)
        propagate_mock.assert_called_once_with(self.root_node)
