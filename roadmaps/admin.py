from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from roadmaps.models import RoadmapNode, Category
from roadmaps.services.progress import ProgressCalculator
from roadmaps.services.roadmap import DownloadIndentedTreeRoadmaps, DownloadRadialTidyTreeRoadmaps


def download_roadmap_radial_tidy_trees(modeladmin, request, queryset):
    return DownloadRadialTidyTreeRoadmaps().download(queryset)


def download_roadmap_indented_trees(modeladmin, request, queryset):
    return DownloadIndentedTreeRoadmaps().download(queryset)


download_roadmap_radial_tidy_trees.short_description = 'Download selected roadmaps as tidy radial trees'
download_roadmap_indented_trees.short_description = 'Download selected roadmaps as indented trees'


class RoadmapNodeAdmin(TreeAdmin):
    form = movenodeform_factory(RoadmapNode)
    list_display = 'name', 'progress',
    search_fields = 'name',
    actions = download_roadmap_radial_tidy_trees, download_roadmap_indented_trees
    filter_horizontal = 'categories',

    def progress(self, obj: RoadmapNode) -> str:
        return ProgressCalculator.calculate(obj)


class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)
    list_display = 'name', 'description',
    search_fields = 'name', 'description',


admin.site.register(RoadmapNode, RoadmapNodeAdmin)
admin.site.register(Category, CategoryAdmin)
