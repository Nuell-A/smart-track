from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Category, Expense, Income, Budget
from .forms import RegistrationForm, CategoryForm, BudgetForm, ExpenseForm, IncomeForm
from decimal import Decimal, ROUND_HALF_UP

# Create your views here.
@login_required
def index(request):
    user = request.user
    # Get totals for user
    total_income = Income.objects.filter(user=user).aggregate(Sum('amount'))['amount__sum']
    total_expenses = Expense.objects.filter(user=user).aggregate(Sum('amount'))['amount__sum']

    # if statements to return 0.00 if there is no amounts yet.
    #else to format to two decimal points and round if needed.
    if total_expenses is None:
        total_expenses = Decimal('0.00')
    else:
        # Format the total expenses to two decimal places
        total_expenses = total_expenses.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP) 

    if total_income is None:
        total_income = Decimal('0.00')
    else:
        # Format the total expenses to two decimal places
        total_income = total_income.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)

    context = {
        'total_income': total_income,
        'total_expenses': total_expenses,
    }

    return render(request, 'index.html', context)

@login_required # Not accessible without logging in. 
def budget(request):
    '''Accepts post requests to add categories.
    If form is submitted correctly, saves the entry into database with 
    logged in user or with default user if no user is logged in.'''

    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        budget_form = BudgetForm(request.POST, user=request.user)
        if category_form.is_valid():
            category = category_form.save(commit=False) # Does not save entry into database yet
            if request.user.is_authenticated: # Checks if user is logged and sets user
                category.user = request.user
            else:
                category.user_id = 1 # If no user is logged in, uses default user
            category.save()
            return redirect('budget')
        
        if budget_form.is_valid():
            budget = budget_form.save(commit=False) # Does not save entry into database yet
            if request.user.is_authenticated: # Checks if user is logged and sets user
                budget.user = request.user
            else:
                budget.user_id = 1 # If no user is logged in, uses default user
            budget.save()
            return redirect('budget')
    else:
        '''Gets logged in user information to display user specific data.'''
        user = request.user
        # Fix categoires to filer by created_by and is_default
        categories = Category.objects.filter(user=user)
        budget_items = Budget.objects.filter(user=user)
        category_form = CategoryForm
        budget_form = BudgetForm(user=request.user)
        context = {
                'category_form': category_form,
                'budget_form': budget_form,
                'categories': categories,
                'budget_items': budget_items,
        }
    return render(request, 'budget.html', context)

@login_required
def expenses(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST, user=request.user) # Passing user to form for filter
        if form.is_valid():
            expense = form.save(commit=False)
            if request.user.is_authenticated:
                expense.user = request.user
            else:
                expense.user_id = 1
            
            expense.save()
            return redirect('expenses')
    else:
        user = request.user
        expenses = Expense.objects.filter(user=user)
        context = {
            'expenses': expenses
        }
        form = ExpenseForm(user=request.user)
    return render(request, 'expenses.html', {'form': form, **context})

@login_required
def income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST) # Passing user to form for filter
        if form.is_valid():
            income = form.save(commit=False)
            if request.user.is_authenticated:
                income.user = request.user
            else:
                income.user_id = 1
            
            income.save()
            print("income saved")
            return redirect('income')
    else:
        user = request.user
        income = Income.objects.filter(user=user)
        context = {
            'income': income
        }
        form = IncomeForm
    return render(request, 'income.html', {'form': form, **context})

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
