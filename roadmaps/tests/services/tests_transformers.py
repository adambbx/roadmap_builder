from django.test import TestCase
from toolz import first

from roadmaps.models import RoadmapNode
from roadmaps.services.transformers import TreeWithProgressTransformer
from roadmaps.types import TreeNode


class SimpleTreeWithProgressTransformerTestCase(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.root_node = RoadmapNode.add_root(name='Introduction to Linear Algebra')
        self.root_node.add_child(name='Learn Vectors')
        self.root_node.add_child(name='Learn Martices')
        self.root_node.refresh_from_db()
        self.tree_dict = first(RoadmapNode.dump_bulk(self.root_node))

    def test_transform(self):
        node = TreeWithProgressTransformer.transform(self.tree_dict)
        self.assertIsInstance(node, TreeNode)
        self.assertEqual(
            node,
            TreeNode(
                name='Introduction to Linear Algebra',
                progress='0/3',
                children=[
                    TreeNode(
                        name='Learn Vectors',
                        progress='0/1',
                        children=[]),
                    TreeNode(
                        name='Learn Martices',
                        progress='0/1',
                        children=[])]))
