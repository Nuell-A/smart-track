from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/registration/', views.registration, name='registration'),
    path('budget/', views.budget, name='budget'),
    path('expenses/', views.expenses, name='expenses'),
    path('income/', views.income, name='income'),
    path('accounts/profile/', views.profile, name='profile'),
]
