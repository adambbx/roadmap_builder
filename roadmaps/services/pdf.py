from roadmaps.services.chrome import ChromeHeadless


class PdfPrinter:

    @staticmethod
    def print(html_filename: str) -> str:
        pdf_filename = html_filename.replace('.html', '.pdf')
        with open(pdf_filename, 'w'):
            ChromeHeadless.print_to_pdf(html_filename, pdf_filename)
            return pdf_filename
