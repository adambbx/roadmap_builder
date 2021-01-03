import os
import zipfile
from io import BytesIO
from typing import List

from toolz import last


class ArchiveInMemory:

    @classmethod
    def create(cls, filenames: List[str]) -> BytesIO:
        buffer = BytesIO()
        with zipfile.ZipFile(buffer, mode='w', compression=zipfile.ZIP_DEFLATED) as archive:
            for f in filenames:
                archive.write(f, arcname=cls._get_arcname(f))
        return buffer

    @classmethod
    def _get_arcname(cls, filename):
        return last(os.path.split(filename))
