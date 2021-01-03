from django.http import HttpResponse
from django.test import TestCase

from roadmaps.models import RoadmapNode
from roadmaps.services.roadmap import DownloadRoadmaps


class DownloadRoadmapTestCase(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.root_node = RoadmapNode.add_root(name='Introduction to Linear Algebra')
        self.first_child = self.root_node.add_child(name='Learn Vectors')
        self.second_child = self.root_node.add_child(name='Learn Martices', is_completed=True)
        self.queryset = RoadmapNode.get_root_nodes().all()

    def test_download(self):
        response = DownloadRoadmaps('roadmaps/hierarchical/indented_tree.html').download(self.queryset)
        self.assertIsInstance(response, HttpResponse)
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.get('Content-Type'), 'application/zip')
        self.assertTrue(len(response.content) > 0)
