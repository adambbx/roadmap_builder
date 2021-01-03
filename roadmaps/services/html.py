from django.shortcuts import render
from toolz import pipe

from roadmaps.models import RoadmapNode
from roadmaps.services.serializers import JsonRoadmapSerializer


class HtmlFileRenderer:

    def __init__(self, tmp_dir: str, template_name: str):
        self._tmp_dir = tmp_dir
        self._template_name = template_name

    def render(self, roadmap_node: RoadmapNode) -> str:
        html_filename = self._get_html_path(roadmap_node)
        with open(html_filename, 'wb') as html_file:
            return self._write(roadmap_node, html_file)

    def _write(self, roadmap_node: RoadmapNode, html_file) -> str:
        content = self._get_html_content(roadmap_node)
        html_file.write(content)
        html_file.flush()
        return html_file.name

    def _get_html_content(self, roadmap_node):
        return pipe(roadmap_node,
                    JsonRoadmapSerializer.serialize,
                    self._render)

    def _render(self, tree_data: str) -> bytes:
        return render(None, self._template_name, context={'treeData': tree_data}).content

    def _get_html_path(self, roadmap_node: RoadmapNode) -> str:
        return f'{self._tmp_dir}/{roadmap_node}.html'
