from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def base(request):
    return render(request, "base.html")

def index(request):
    return render(request, "index.html")