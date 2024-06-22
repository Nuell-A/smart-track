from django.contrib import admin
from .models import Category, Budget, Expense, Income

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('category', 'amount',)
    search_fields = ('category',)

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'amount', 'date',)
    search_fields = ('category', 'date')

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'date',)
    search_fields = ('name', 'date',)
