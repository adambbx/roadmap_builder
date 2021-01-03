import tempfile

from django.db.models import QuerySet
from django.http import HttpResponse
from toolz import pipe
from toolz.curried import map

from roadmaps.models import RoadmapNode
from roadmaps.services.archive import ArchiveInMemory
from roadmaps.services.html import HtmlFileRenderer
from roadmaps.services.http import HttpResponseHelper
from roadmaps.services.pdf import PdfPrinter


class DownloadRoadmaps:

    def __init__(self, template_name: str):
        self._template_name = template_name

    def download(self, queryset: QuerySet[RoadmapNode]) -> HttpResponse:
        with tempfile.TemporaryDirectory() as tmp_dir:
            html = HtmlFileRenderer(tmp_dir, self._template_name)
            return pipe(queryset,
                        map(html.render),
                        map(PdfPrinter.print),
                        ArchiveInMemory.create,
                        HttpResponseHelper.get_download_response)


class DownloadIndentedTreeRoadmaps(DownloadRoadmaps):

    def __init__(self):
        super().__init__('roadmaps/hierarchical/indented_tree.html')


class DownloadRadialTidyTreeRoadmaps(DownloadRoadmaps):

    def __init__(self):
        super().__init__('roadmaps/hierarchical/radial_tidy_tree.html')
