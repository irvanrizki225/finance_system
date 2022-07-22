from dataclasses import field, fields
from django import forms
from django.forms import ModelForm
from .models import Transaction

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in fields(self.Meta.model):
    #         self.fields[field.name].widget.attrs.update({'class': 'form-control'})
    #         self.fields[field.name].widget.attrs.update({'placeholder': field.name})
    #         self.fields[field.name].label = field.name
    #         self.fields[field.name].help_text = field.name
    #         self.fields[field.name].required = True
    #         if field.name == 'date_in':
    #             self.fields[field.name].widget.attrs.update({'type': 'date'})
    #         if field.name == 'date_out':
    #             self.fields[field.name].widget.attrs.update({'type': 'date'})
    #         if field.name == 'amount':
    #             self.fields[field.name].widget.attrs.update({'type': 'number'})
    #         if field.name == 'total':
    #             self.fields[field.name].widget.attrs.update({'type': 'number'})
    #         if field.name == 'type':
    #             self.fields[field.name].widget.attrs.update({'type': 'text'})
    #         if field.name == 'name':
    #             self.fields[field.name].widget.attrs.update({'type': 'text'})
    #         if field.name == 'user':
    #             self.fields[field.name].widget.attrs.update({'type': 'hidden'})
    #         if field.name == 'id':
    #             self.fields[field.name].widget.attrs.update({'type': 'hidden'})
    #         if field.name == 'created_at':
    #             self.fields[field.name].widget.attrs.update({'type': 'hidden'})
    #         if field.name == 'updated_at':
    #             self.fields[field.name].widget.attrs.update({'type': 'hidden'})
    #         if field.name == 'deleted_at':
    #             self.fields[field.name].widget.attrs.update({'type': 'hidden'})

    # def clean(self):
    #     cleaned_data = super().clean()
    #     return cleaned_data
    