from webbrowser import get
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404, HttpResponsePermanentRedirect
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
    # model = Transaction
    template_name = 'transaction/transaction_detail.html'
    # context_object_name = 'transaction'
    queryset = Transaction.objects.all()

    def get_object(self):
        Transaction = super().get_object()
        return Transaction

# create transaction
class TransactionCreateView(CreateView):
    model = Transaction
    template_name = 'transaction/transaction_form.html'
    fields = ['account', 'amount', 'type', 'date_in', 'date_out', 'total', 'user_id']

    def get_queryset(self):
        return Transaction.objects.all()
