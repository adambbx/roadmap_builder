from io import BytesIO

from django.http import HttpResponse
from django.test import TestCase

from roadmaps.services.http import HttpResponseHelper


class HttpResponseHelperTestCase(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.content = b'hello world'
        self.buffer = BytesIO(b'hello world')

    def test_get_download_response(self):
        response = HttpResponseHelper.get_download_response(self.buffer)
        self.assertIsInstance(response, HttpResponse)
        self.assertEqual(200, response.status_code)
        self.assertEqual(self.content, response.content)
        self.assertEqual(response.get('Content-Disposition'), 'attachment; filename=roadmaps.zip')
        self.assertEqual(response.get('Content-Type'), 'application/zip')
