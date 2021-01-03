from django.http import JsonResponse


# Create your views here.


def save_svg_content_to_file(request):
    request.POST.get('')

    return JsonResponse({'message': 'success'})
