from django.contrib import admin
from .models import Category, Budget

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Budget)
class CategoryExpense(admin.ModelAdmin):
    list_display = ('category', 'amount',)
    search_fields = ('category',)