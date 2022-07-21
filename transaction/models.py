from django.db import models

# Create your models here.

class Transaction(models.Model):
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    type = models.CharField(max_length=10)
    date_in = models.DateField()
    date_out = models.DateField()
    total = models.IntegerField()

    def __str__(self):
        return self.name

class Debit(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    date = models.DateField()

    def __str__(self):
        return self.name

class Credit(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    date = models.DateField()
    
    def __str__(self):
        return self.name