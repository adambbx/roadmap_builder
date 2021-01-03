from django.conf import settings
from django.contrib.staticfiles.finders import find
from django.contrib.staticfiles.storage import staticfiles_storage, StaticFilesStorage, HashedFilesMixin
from django.utils.safestring import mark_safe


class InlineStaticService:

    def get_inline_static(self, name: str) -> str:
        return mark_safe(self._from_app_directory(name)
                         if settings.DEBUG
                         else self._from_staticfiles_storage(name))

    def _from_app_directory(self, name):
        with open(find(name), 'r') as static_file:
            return static_file.read()

    def _from_staticfiles_storage(self, name):
        path = staticfiles_storage.stored_name(name) if self._is_hashed(staticfiles_storage) else name
        if staticfiles_storage.exists(path):
            with staticfiles_storage.open(path, 'r') as static_file:
                return static_file.read()

    def _is_hashed(self, storage: StaticFilesStorage) -> bool:
        return isinstance(storage, HashedFilesMixin)
