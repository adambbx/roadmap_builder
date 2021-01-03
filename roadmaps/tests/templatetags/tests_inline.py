from unittest import mock

from django.test import TestCase

from roadmaps.services.inline import InlineStaticService
from roadmaps.templatetags.inline import inline_javascript, inline_css


class InlineJavascriptTagTestCase(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.expected_content = 'safe inline content'
        self.filename = 'js/test.js'

    @mock.patch.object(InlineStaticService, 'get_inline_static')
    def test_inline_javascript(self, get_inline_static_mock):
        get_inline_static_mock.return_value = self.expected_content
        self.assertEqual(
            {'js_content': 'safe inline content'},
            inline_javascript(self.filename))
        get_inline_static_mock.assert_called_once_with(self.filename)


class InlineCssTagTestCase(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.expected_content = 'safe inline content'
        self.filename = 'css/test.css'

    @mock.patch.object(InlineStaticService, 'get_inline_static')
    def test_inline_javascript(self, get_inline_static_mock):
        get_inline_static_mock.return_value = self.expected_content
        self.assertEqual(
            {'css_content': 'safe inline content'},
            inline_css(self.filename))
        get_inline_static_mock.assert_called_once_with(self.filename)
