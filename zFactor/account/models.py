from django.db import models
from soft_delete_it.models import SoftDeleteModel
from django.contrib.auth.models import User
from invoice.models import Invoice
from payment.models import Receipt
from disbursement.models import DisbursementRequest
from account_management.models import OverAdvance, MiscCharge



class AccountType(SoftDeleteModel): # Asset, liablity, capital
    account_type_id = models.AutoField(primary_key = True, auto_created = True)
    account_type_name = models.CharField(max_length=100, default=None, blank=True, null=True)
    account_type_description = models.CharField(max_length=255, default=None, blank=True, null=True)
    
class Account(SoftDeleteModel):
    account_id = models.AutoField(primary_key = True, auto_created = True)
    account_number = models.CharField(max_length=100, default=None, blank=True, null=True) # Mapped account in accounting software
    account_name = models.CharField(max_length=100, default=None, blank=True, null=True)
    account_description = models.CharField(max_length=255, default=None, blank=True, null=True)
    account_type = models.ForeignKey(AccountType, on_delete=models.PROTECT)
    
class TransactionSource(SoftDeleteModel): #Invoice, Receipt, Disbursement, over advance, Payment application, over advance, misc charges, writeoff
    transaction_source_id = models.AutoField(primary_key = True, auto_created = True)
    transaction_source_name = models.CharField(max_length=100, default=None, blank=True, null=True)
    transaction_source_description = models.CharField(max_length=255, default=None, blank=True, null=True)
    
class TransactionType(SoftDeleteModel): # Purchase , Fuel advance, payment, over advance, writeoff, invoice adjustment, fee adjustment, reversal of payment
    transaction_type_id = models.AutoField(primary_key = True, auto_created = True)
    transaction_type_name = models.CharField(max_length=100, default=None, blank=True, null=True)
    transaction_type_description = models.CharField(max_length=255, default=None, blank=True, null=True)
    
class Transaction(SoftDeleteModel):
    transaction_id = models.AutoField(primary_key = True, auto_created = True)
    transaction_source = models.ForeignKey(TransactionSource, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    invoice = models.ForeignKey(Invoice,default=None, blank=True, null=True, on_delete=models.CASCADE)
    receipt = models.ForeignKey(Receipt,default=None, blank=True, null=True, on_delete=models.CASCADE)
    over_advance = models.ForeignKey(OverAdvance,default=None, blank=True, null=True, on_delete=models.CASCADE)
    disbursement = models.ForeignKey(DisbursementRequest,default=None, blank=True, null=True, on_delete=models.CASCADE)
    misc_charges = models.ForeignKey(MiscCharge,default=None, blank=True, null=True, on_delete=models.CASCADE)
    transaction_type = models.ForeignKey(TransactionType,default=None, blank=True, null=True, on_delete=models.PROTECT)
    transaction_note = models.CharField(max_length=255, default=None, blank=True, null=True)
    
class Ledger(SoftDeleteModel):
    ledger_id = models.AutoField(primary_key = True, auto_created = True)
    Transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    credit = models.DecimalField(max_digits=11, decimal_places=2)
    debit = models.DecimalField(max_digits=11, decimal_places=2)
    
