from django.shortcuts import render, redirect
from .models import Category
from .forms import RegistrationForm

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

def registration(request):
    print("loading registration")
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm
    return render(request, 'registration.html', {'form': form})

def profile(request):
    '''Insert profile template and other information here once users login.'''
    pass
