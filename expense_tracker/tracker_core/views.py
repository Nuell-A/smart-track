from django.shortcuts import render
from .models import Category

# Create your views here.
def index(request):
    print("loading page")
    return render(request, 'index.html')