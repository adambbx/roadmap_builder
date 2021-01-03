import os
import tempfile

from django.test import TestCase

from roadmaps.models import RoadmapNode
from roadmaps.services.html import HtmlFileRenderer


class HtmlFileRendererTestCase(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.roadmap_node = RoadmapNode.add_root(name='Root')

    def test_render(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            html_renderer = HtmlFileRenderer(tmp_dir, 'roadmaps/hierarchical/radial_tidy_tree.html')
            filename = html_renderer.render(self.roadmap_node)
            self.assertTrue(os.path.getsize(filename) > 0)
