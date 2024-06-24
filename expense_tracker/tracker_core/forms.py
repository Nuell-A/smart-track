from django import forms
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
