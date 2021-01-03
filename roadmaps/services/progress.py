from typing import List

from roadmaps.models import RoadmapNode


class ProgressCalculator:

    @classmethod
    def calculate(cls, roadmap: RoadmapNode) -> str:
        completion_rate = cls._check_completion_rate(roadmap)
        return f'{completion_rate.count(True)}/{len(completion_rate)}'

    @classmethod
    def _check_completion_rate(cls, roadmap: RoadmapNode) -> List[bool]:
        return [d.is_completed for d in roadmap.get_descendants()] + [roadmap.is_completed]


class ProgressPropagator:

    @classmethod
    def propagate_completion_desc(cls, roadmap: RoadmapNode) -> None:
        roadmap \
            .get_descendants() \
            .filter(is_completed=not roadmap.is_completed) \
            .update(is_completed=roadmap.is_completed)
