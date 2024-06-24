from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Expense
from .forms import RegistrationForm, CategoryForm

# Create your views here.
def index(request):
    print("loading dashboard")
    print(request.user)
    print(request.user.is_authenticated)
    return render(request, 'index.html')

@login_required # Not accessible without logging in. 
def budget(request):
    '''Accepts post requests to add categories.
    If form is submitted correctly, saves the entry into database with 
    logged in user or with default user if no user is logged in.'''

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False) # Does not save entry into database yet
            if request.user.is_authenticated: # Checks if user is logged and sets user
                category.user = request.user
            else:
                category.user_id = 1 # If no user is logged in, uses default user
            
            category.save()
            return redirect('budget')
        else:
            print("there was an error with the form")
    else:
        '''Gets logged in user information to display user specific data.'''
        user = request.user
        categories = Category.objects.filter(user=user)
        expenses = Expense.objects.filter(user=user)
        context = {
                'categories': categories,
                'expenses': expenses
        }
        form = CategoryForm
    return render(request, 'budget.html', {'form': form, **context})

@login_required
def expenses(request):
    print("loading expenses")
    return render(request, 'expenses.html')

@login_required
def income(request):
    print("loading income")
    return render(request, 'income.html')

def registration(request):
    print("loading registration")
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid(): # Saves user if form is correct.
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm
    return render(request, 'accounts/registration.html', {'form': form})
@login_required
def profile(request):
    '''Insert profile template and other information here once users login.'''
    return render(request, 'accounts/profile.html',)
