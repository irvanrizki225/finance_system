from asyncio.windows_events import NULL
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404

from .models import Transaction
from .forms import TransactionForm

def index(request):
    transactions = Transaction.objects.all()
    return render(request, 'page/transaction/index.html', {'transactions': transactions})

def create(request):
    last_transaction = Transaction.objects.last()
    if request.method == 'POST':

        if last_transaction == None:
            total = request.POST['amount']
        else:
            if request.POST['type'] == 'Debit':
                total = int(last_transaction.total)+int(request.POST['amount'])
            else:
                 total = int(last_transaction.total) - int(request.POST['amount'])

        if request.POST['date_in'] == '':
            date_in = NULL
        else:
           date_in = request.POST['date_in']


        if request.POST['date_out'] == '':
            date_out = NULL
        else:
            date_out = request.POST['date_out']


        post = Transaction()
        post.user = request.user
        post.name = ''.join(request.POST['name'])
        post.amount = request.POST['amount']
        post.type = request.POST['type']
        post.date_in = date_in
        post.date_out = date_out
        post.total = int(total)
        post.save()
        return HttpResponseRedirect('/transaction/')
        # return render(total)
        
    else:
        form = TransactionForm()
    return render(request, 'page/transaction/create.html', {'form': form})

def update(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/transaction/')
    else:
        form = TransactionForm(instance=transaction)
        return render(request, 'page/transaction/update.html', {'form': form})

def delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    transaction.delete()
    return redirect('/transaction/')