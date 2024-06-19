from django.shortcuts import render

# Create your views here.
def index(request):
    print("loading page")
    return render(request, 'index.html')