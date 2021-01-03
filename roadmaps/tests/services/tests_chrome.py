import os
import tempfile
from unittest import TestCase

from roadmaps.services.chrome import ChromeHeadless


class ChromeHeadlessTestCase(TestCase):

    def test_print_to_pdf(self):
        with tempfile.NamedTemporaryFile() as html_file, tempfile.NamedTemporaryFile(delete=False) as pdf_file:
            html_file.write(b'<html>Hello world!</html>')
            html_file.flush()
            ChromeHeadless.print_to_pdf(html_file.name, pdf_file.name)
            self.assertTrue(os.path.getsize(pdf_file.name) > 0)
