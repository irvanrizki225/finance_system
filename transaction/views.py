from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404, redirect
from .models import Transaction


# list transactions
class TransactionListView(ListView):
    model = Transaction
    template_name = 'transaction/transaction_list.html'
    context_object_name = 'transaction_list'

    def get_queryset(self):
        return  Transaction.objects.all()

# detail transaction
class TransactionDetailView(DetailView):
    model = Transaction
    template_name = 'transaction/transaction_detail.html'
    context_object_name = 'transaction'

    def get_queryset(self):
        self.transaction = get_object_or_404(Transaction, pk=self.kwargs['pk'])
        return Transaction.objects.all()

# create transaction
class TransactionCreateView(CreateView):
    model = Transaction
    template_name = 'transaction/transaction_form.html'
    fields = ['account', 'amount', 'type', 'description']

    def get_queryset(self):
        return Transaction.objects.all()