# from django.http import HttpResponse
from django.shortcuts import HttpResponse, render

# Create your views here.
def test_view(request):
    return HttpResponse("Hello, this is a test view!")

def html_view(request):
    return render(request, "base.html")