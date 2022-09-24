# Create your views here.
from django.shortcuts import render


# This function will render the Home page when requested
def home(request):
    return render(request, 'checkbook/index.html')


# This function will render render the Create New Account page when requested
def create_account(request):
    return render(request, 'checkbook/CreateNewAccount.html')


# This function will render the Balance page when requested
def balance(request):
    return render(request, 'checkbook/BalanceSheet.html')


# This function will render the Transaction page when requested
def transaction(request):
    return render(request, 'checkbook/AddTransaction.html')