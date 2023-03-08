from django.template import loader
from django.http import HttpResponse


def test(request):
    return HttpResponse("Hello, world. You're at the polls index.")
