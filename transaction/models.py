from django.db import models

# Create your models here.

class Transaction(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    type = models.CharField(max_length=10)
    date_in = models.DateField(null=True)
    date_out = models.DateField(null=True)
    total = models.IntegerField()

    def __str__(self):
        return self.name

class Debit(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    image = models.ImageField(upload_to='images/',null=True)
    date = models.DateField()

    def __str__(self):
        return self.name

class Credit(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    image = models.ImageField(upload_to='images/',null=True)
    date = models.DateField()
    
    def __str__(self):
        return self.name