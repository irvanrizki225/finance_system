from webbrowser import get
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404, HttpResponsePermanentRedirect
from .models import Transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TransactionForm


# list transactions
class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'page/transaction/index.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        return  Transaction.objects.filter(user=self.request.user.is_authenticated).all()

# # detail transaction
# class TransactionDetailView(DetailView):
#     # model = Transaction
#     template_name = 'transaction/transaction_detail.html'
#     # context_object_name = 'transaction'
#     queryset = Transaction.objects.all()

#     def get_object(self):
#         Transaction = super().get_object()
#         return Transaction

# create transaction
class TransactionCreateView(CreateView):
    model = Transaction
    template_name = 'page/transaction/create.html'
    fields = [ 'name', 'amount', 'type', 'date_in', 'date_out', 'total']
    success_url = '/transaction/'
    forms = TransactionForm

    def get_queryset(self):
        return Transaction.objects.all()

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# update transaction
class TransactionUpdateView(UpdateView):
    model = Transaction
    template_name = 'page/transaction/update.html'
    fields = [ 'name', 'amount', 'type', 'date_in', 'date_out', 'total']
    forms = TransactionForm
    success_url = '/transaction/'

    def get_queryset(self):
        return Transaction.objects.all()

    def get_object(self):
        Transaction = super().get_object()
        return Transaction

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# delete transaction
class TransactionDeleteView(DeleteView):
    model = Transaction
    success_url = '/transaction/'

    
