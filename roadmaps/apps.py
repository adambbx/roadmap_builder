from django.apps import AppConfig


class RoadmapsConfig(AppConfig):
    name = 'roadmaps'

    def ready(self):
        import roadmaps.signal_listeners


