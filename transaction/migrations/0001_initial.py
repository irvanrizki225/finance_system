# Generated by Django 4.0.6 on 2022-07-21 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('type', models.CharField(max_length=10)),
                ('date_in', models.DateField()),
                ('date_out', models.DateField()),
                ('total', models.IntegerField()),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
        ),
        migrations.CreateModel(
            name='Debit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/')),
                ('date', models.DateField()),
                ('id_transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/')),
                ('date', models.DateField()),
                ('id_transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.transaction')),
            ],
        ),
    ]