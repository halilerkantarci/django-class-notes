from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
    print(request)
    print(request.method)
    html = "<html><body><h1>hello from the other side.</h1></body></html>"
    return HttpResponse(html)

