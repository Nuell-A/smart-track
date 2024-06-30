from django import forms
from django.forms.widgets import DateInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Category, Budget, Expense, Income

'''Forms for models. Used to create entries into database.'''

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ('name',)

class BudgetForm(forms.ModelForm):

    class Meta:
        model = Budget
        fields = ('amount', 'category',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user)

class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = ('name', 'amount', 'category', 'date',)
        widgets = {
            'date': DateInput(attrs={'type': 'date'})
        }

    # Used to filter categories by user, this way users 
    #don't see each other categories
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user)

class IncomeForm(forms.ModelForm):

    class Meta:
        model = Income
        fields = ('name', 'amount', 'date',)
        widgets = {
            'date': DateInput(attrs={'type': 'date'})
        }