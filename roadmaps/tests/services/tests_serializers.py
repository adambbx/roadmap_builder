from django.test import TestCase

from roadmaps.models import RoadmapNode
from roadmaps.services.serializers import JsonRoadmapSerializer


class JsonRoadmapSerializerTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.roadmap_node = RoadmapNode.add_root(name='Test Root')
        self.roadmap_node.add_child(name='First child')
        self.roadmap_node.add_child(name='Second child')

    def test_serialize(self):
        self.assertEqual(
            JsonRoadmapSerializer.serialize(self.roadmap_node),
            '{"name": "Test Root", "progress": "0/3", '
            '"children": [{"name": "First child", "progress": "0/1", '
            '"children": []}, {"name": "Second child", "progress": "0/1", "children": []}]}')
