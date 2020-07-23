from django.db import models
from django.urls import reverse
from soft_delete_it.models import SoftDeleteModel
from client.models import Client,Terms,FundingAccount
from debtor.models import Debtor

# Create your models here.

class RequestType(SoftDeleteModel): #Wire, ACH, Check...
    request_type_id = models.AutoField(auto_created=True, primary_key=True)
    request_type = models.CharField(max_length=50, default=None, blank=True, null=True)
    description = models.CharField(max_length=255, default=None, blank=True, null=True)
    
    def __str__(self):
        return self.request_type


class DisbursementRequest(SoftDeleteModel):
    request_id = models.AutoField(auto_created=True, primary_key=True)
    request_type = models.ForeignKey(RequestType, on_delete=models.PROTECT)
    funding_account = models.ForeignKey(FundingAccount, on_delete=models.PROTECT)
    client = models.ForeignKey(Client, default=None, blank=True, null=True, on_delete=models.PROTECT)
    amount = models.DecimalField(decimal_places=2, max_digits=11)   
    date_requested = models.DateTimeField(auto_now_add=True, blank=True)
    reference_number = models.CharField(max_length=255, default=None, blank=True, null=True)
    check_number = models.CharField(max_length=50, default=None, blank=True, null=True)
    check_date = models.DateTimeField(default=None, blank=True, null=True)
    is_granted = models.BooleanField(default=False) # Request granted by Factor
    is_cleared = models.BooleanField(default=False) # Fund withdrown from Factor's bank/other account
    notes = models.CharField(max_length=255, default=None, blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse('disbursement_requet_detail', kwargs={'id':self.request_id})
    
    
class Transcheck(SoftDeleteModel):
    transcheck_id = models.AutoField(auto_created=True, primary_key=True)
    request = models.ForeignKey(DisbursementRequest, default=None, blank=True, null=True, on_delete=models.PROTECT)
    account_number  = models.CharField(max_length=50, default=None, blank=True, null=True)
    batch_number = models.CharField(max_length=50, default=None, blank=True, null=True)
    transaction_number = models.CharField(max_length=50, default=None, blank=True, null=True)
    book_number = models.CharField(max_length=50, default=None, blank=True, null=True) 
    expiration_date = models.DateTimeField(default=None, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    code_used = models.BooleanField(default=False)
    money_code = models.CharField(max_length=50, default=None, blank=True, null=True)