import subprocess

from roadmap_builder import settings


class ChromeHeadless:

    @classmethod
    def print_to_pdf(cls, html_filename: str, output_file: str) -> None:
        subprocess.call(cls._get_command(html_filename, output_file))

    @classmethod
    def _get_command(cls, html_filename, output_file):
        return [settings.CHROME_BINARY_PATH,
                '--headless',
                '--no-sandbox',
                '--disable-gpu',
                '--disable-extensions',
                '--virtual-time-budget=5000',
                f'--print-to-pdf={output_file}',
                f'file://{html_filename}']
