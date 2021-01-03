from unittest import mock

from django.conf import settings
from django.contrib.staticfiles.storage import ManifestStaticFilesStorage
from django.core.files.base import ContentFile
from django.test import TestCase, override_settings

from roadmaps.services.inline import InlineStaticService


class InlineStaticServiceTestCase(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.filename = 'js/d3.v6.js'
        with open(settings.BASE_DIR / 'roadmaps/static' / self.filename, 'r') as js_file:
            self.expected_content = js_file.read()
        self.inline_static_service = InlineStaticService()

    @override_settings(DEBUG=True)
    def test_get_inline_static_debug_enabled(self):
        self.assertEqual(self.inline_static_service.get_inline_static('js/d3.v6.js'), self.expected_content)

    @override_settings(DEBUG=False)
    def test_get_inline_static_debug_disabled(self):
        self.assertEqual(self.inline_static_service.get_inline_static('js/d3.v6.js'), self.expected_content)

    @override_settings(DEBUG=False)
    def test_get_inline_static_hashed_storage(self):
        hashed_storage_stub = mock.create_autospec(ManifestStaticFilesStorage)
        hashed_storage_stub.stored_name.return_value = self.filename
        hashed_storage_stub.exists.return_value = True
        hashed_storage_stub.open.return_value = ContentFile(self.expected_content)
        with mock.patch('roadmaps.services.inline.staticfiles_storage', new=hashed_storage_stub):
            self.assertEqual(self.inline_static_service.get_inline_static(self.filename), self.expected_content)
