from io import BytesIO

from django.http import HttpResponse


class HttpResponseHelper:
    filename = 'roadmaps.zip'
    content_type = 'application/zip'

    @classmethod
    def get_download_response(cls, buffer: BytesIO) -> HttpResponse:
        response = HttpResponse(buffer.getvalue(), content_type=cls.content_type)
        response['Content-Disposition'] = f'attachment; filename={cls.filename}'
        return response
