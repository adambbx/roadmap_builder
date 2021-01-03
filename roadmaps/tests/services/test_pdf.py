import tempfile
from unittest import mock

from django.test import TestCase

from roadmaps.services.chrome import ChromeHeadless
from roadmaps.services.pdf import PdfPrinter


class PdfPrinterTestCase(TestCase):

    @mock.patch.object(ChromeHeadless, 'print_to_pdf')
    def test_print(self, print_to_pdf_mock):
        with tempfile.TemporaryDirectory() as tmp_dir:
            html_filename = f'{tmp_dir}/test.html'
            pdf_filename = PdfPrinter.print(html_filename)
            print_to_pdf_mock.assert_called_once_with(html_filename, pdf_filename)
