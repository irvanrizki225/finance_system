# Generated by Django 4.0.6 on 2022-07-21 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='credit',
            old_name='id_transaction',
            new_name='transaction_id',
        ),
        migrations.RenameField(
            model_name='debit',
            old_name='id_transaction',
            new_name='transaction_id',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='id_user',
            new_name='user_id',
        ),
    ]
