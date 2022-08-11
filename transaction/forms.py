from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [ 'user' , 'name', 'amount', 'type', 'date_in', 'date_out']
        # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-6', 'placeholder': 'User'}))
        date_in = forms.DateField(required=False)
        date_out = forms.DateField(required=False)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'Amount'}),
            'date_in': forms.DateInput(attrs={'type': 'date'}),
            'date_out': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'user': 'User',
            'name': 'Name',
            'amount': 'Amount',
            'type': 'Type',
            'date_in': 'Date In',
            'date_out': 'Date Out',
        }
        help_texts = {
            'user': 'Enter the User of the transaction',
            'name': 'Enter the name of the transaction',
            'amount': 'Enter the amount of the transaction',
            'type': 'Enter the type of the transaction',
            'date_in': 'Enter the date in of the transaction',
            'date_out': 'Enter the date out of the transaction',
        }
        error_messages = {
            'user': {
                'required': 'User is required',
            },
            'name': {
                'max_length': "This field has max length of 100 characters",
                'required': "This field is required",
            },
            'amount': {
                'required': "This field is required",
            },
            'type': {
                'required': "This field is required",
            },
        }