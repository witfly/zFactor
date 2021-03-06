# Generated by Django 3.0.8 on 2020-07-22 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisbursementRequest',
            fields=[
                ('request_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('deleted', models.UUIDField(blank=True, default=None, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('date_requested', models.DateTimeField(auto_now_add=True)),
                ('reference_number', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('check_number', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('check_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('is_granted', models.BooleanField(default=False)),
                ('is_cleared', models.BooleanField(default=False)),
                ('notes', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('client', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='client.Client')),
                ('funding_account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client.FundingAccount')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RequestType',
            fields=[
                ('request_type_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('deleted', models.UUIDField(blank=True, default=None, null=True)),
                ('request_type', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('description', models.CharField(blank=True, default=None, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transcheck',
            fields=[
                ('transcheck_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('deleted', models.UUIDField(blank=True, default=None, null=True)),
                ('account_number', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('batch_number', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('transaction_number', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('book_number', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('expiration_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('code_used', models.BooleanField(default=False)),
                ('money_code', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('request', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='disbursement.DisbursementRequest')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='disbursementrequest',
            name='request_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='disbursement.RequestType'),
        ),
    ]
