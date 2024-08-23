from django.shortcuts import render, get_object_or_404, redirect
from .models import Account

def list_accounts(request):
    accounts = Account.objects.all()
    return render(request, 'account/list.html', {'accounts': accounts})

def account_detail(request, pk):
    account = get_object_or_404(Account, pk=pk)
    return render(request, 'account/detail.html', {'account': account})

def update_account(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        new_name = request.POST.get('name')
        new_email = request.POST.get('email')
        account.name = new_name
        account.email = new_email
        account.save()
        return redirect('list_accounts')
    return render(request, 'account/update.html', {'account': account})

def delete_account(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        account.delete()
        return redirect('list_accounts')
    return render(request, 'account/confirm_delete.html', {'account': account})

def create_account(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        Account.objects.create(name=name, email=email)
        return redirect('list_accounts')
    return render(request, 'account/create.html')
