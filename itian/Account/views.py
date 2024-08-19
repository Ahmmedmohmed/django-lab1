



from django.shortcuts import render
from django.http import HttpResponse

ACCOUNTS = [
    {'id': 1, 'name': 'Ahmed Ali', 'email': 'ahmed@gmail.com'},
    {'id': 2, 'name': 'Sara mohmed', 'email': 'sara@gmail.com'},
]

def list_accounts(request):
    return render(request, 'account/list.html', {'accounts': ACCOUNTS})




def account_detail(request, pk):
    account = next((acc for acc in ACCOUNTS if acc['id'] == pk), None)
    return render(request, 'account/detail.html', {'account': account})


    # account/views.py

def update_account(request, pk):
    account = next((acc for acc in ACCOUNTS if acc['id'] == pk), None)
    if request.method == 'POST':
        new_name = request.POST.get('name')
        new_email = request.POST.get('email')
        if account:
            account['name'] = new_name
            account['email'] = new_email
    return render(request, 'account/update.html', {'account': account})


    # account/views.py

def delete_account(request, pk):
    global ACCOUNTS
    ACCOUNTS = [acc for acc in ACCOUNTS if acc['id'] != pk]
    return render(request, 'account/list.html', {'accounts': ACCOUNTS})


from django.http import HttpResponse

def create_account(request):
    return HttpResponse("Account created")
