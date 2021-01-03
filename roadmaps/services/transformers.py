from typing import Union, List, Dict

from toolz import get_in

from roadmaps.models import RoadmapNode
from roadmaps.services.progress import ProgressCalculator
from roadmaps.types import TreeNode


class TreeWithProgressTransformer:

    @classmethod
    def transform(cls, node: Dict[str, Union[str, List[TreeNode]]]):
        name = get_in(['data', 'name'], node)
        return TreeNode(
            name=name,
            progress=ProgressCalculator.calculate(RoadmapNode.objects.get(name=name)),
            children=[cls.transform(ch) for ch in node.get('children', [])])
