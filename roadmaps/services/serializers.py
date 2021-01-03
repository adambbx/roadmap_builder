import json
from dataclasses import asdict

from toolz import pipe, first

from roadmaps.models import RoadmapNode
from roadmaps.services.transformers import TreeWithProgressTransformer


class JsonRoadmapSerializer:

    @classmethod
    def serialize(cls, roadmap_node: RoadmapNode) -> str:
        return pipe(roadmap_node,
                    RoadmapNode.dump_bulk,
                    first,
                    TreeWithProgressTransformer.transform,
                    asdict,
                    json.dumps)
