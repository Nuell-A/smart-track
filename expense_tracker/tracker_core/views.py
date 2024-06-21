from django.shortcuts import render
from .models import Category

# Create your views here.
def index(request):
    print("loading dashboard")
    return render(request, 'index.html')

def budget(request):
    print("loading budget")
    return render(request, 'budget.html')

def expenses(request):
    print("loading expenses")
    return render(request, 'expenses.html')

def income(request):
    print("loading income")
    return render(request, 'income.html')
