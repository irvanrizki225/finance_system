from urllib import request
from django.shortcuts import redirect, render
from django.http import Http404
from django.contrib import messages

from transaction.models import Transaction, Debit, Credit

def index(request):
    transaction_detail = Transaction.objects.select_related('user').all()
    debit = Debit.objects.all()
    credit = Credit.objects.all()
    context = {
        'transaction_detail': transaction_detail,
        'debit': debit,
        'credit': credit,
    }

    return render(request, 'core/index.html', context)