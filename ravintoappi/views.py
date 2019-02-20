from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    etusivu = "<html><body>Hae elintarviketta</body></html>"
    return HttpResponse(etusivu)
