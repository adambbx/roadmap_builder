from django.test import TestCase

from roadmaps.models import RoadmapNode
from roadmaps.services.progress import ProgressCalculator, ProgressPropagator


class ProgressCalculatorTestCase(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.root_node = RoadmapNode.add_root(name='Introduction to Linear Algebra')
        self.first_child = self.root_node.add_child(name='Learn Vectors')
        self.second_child = self.root_node.add_child(name='Learn Martices', is_completed=True)

    def test_calculate_none_completed(self):
        self.assertEqual('1/3', ProgressCalculator.calculate(self.root_node))
        self.assertEqual('0/1', ProgressCalculator.calculate(self.first_child))
        self.assertEqual('1/1', ProgressCalculator.calculate(self.second_child))


class ProgressPropagatorTestCase(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.root_node = RoadmapNode.add_root(name='Introduction to Linear Algebra')
        self.first_child = self.root_node.add_child(name='Learn Vectors')
        self.second_child = self.root_node.add_child(name='Learn Martices', is_completed=True)

    def test_propagate_completion_true_desc(self):
        self.root_node.is_completed = True
        ProgressPropagator.propagate_completion_desc(self.root_node)
        self.assertTrue(all(n.is_completed for n in self.root_node.get_descendants()))

    def test_propagate_completion_false_desc(self):
        self.root_node.is_completed = True
        self.root_node.save()
        self.root_node.is_completed = False
        ProgressPropagator.propagate_completion_desc(self.root_node)
        self.assertFalse(any(n.is_completed for n in self.root_node.get_descendants()))
