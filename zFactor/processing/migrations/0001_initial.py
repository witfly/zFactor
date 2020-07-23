# Generated by Django 3.0.8 on 2020-07-22 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceHoldReason',
            fields=[
                ('invoice_hold_reason_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('deleted', models.UUIDField(blank=True, default=None, null=True)),
                ('hold_name', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('hold_description', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProcessingNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.UUIDField(blank=True, default=None, null=True)),
                ('note', models.CharField(max_length=255)),
                ('is_alert', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('show_client', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('hold_reason', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='processing.InvoiceHoldReason')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processing_note', to='invoice.Invoice')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
