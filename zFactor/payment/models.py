from django.db import models
from django.urls import reverse
from soft_delete_it.models import SoftDeleteModel
from client.models import Client,Terms
from debtor.models import Debtor

# Create your models here.

class ReceiptType(SoftDeleteModel): #Wire, ACH, Check...
    receipt_type_id = models.AutoField(auto_created=True, primary_key=True)
    receipt_type = models.CharField(max_length=50, default=None, blank=True, null=True)
    description = models.CharField(max_length=255, default=None, blank=True, null=True)
    
    def __str__(self):
        return self.receipt_type


class Receipt(SoftDeleteModel):
    receipt_id = models.AutoField(auto_created=True, primary_key=True)
    batch_number = models.CharField(max_length=255, default=None, blank=True, null=True)
    receipt_type = models.ForeignKey(ReceiptType, on_delete=models.PROTECT)
    client = models.ForeignKey(Client, default=None, blank=True, null=True, on_delete=models.PROTECT)
    debtor = models.ForeignKey(Debtor, default=None, blank=True, null=True, on_delete=models.PROTECT)
    amount = models.DecimalField(default=0, decimal_places=2, max_digits=11)   
    date_received = models.DateTimeField(auto_now_add=True, blank=True)
    reference_number = models.CharField(max_length=255, default=None, blank=True, null=True)
    check_number = models.CharField(max_length=50, default=None, blank=True, null=True)
    check_date = models.DateTimeField(default=None, blank=True, null=True)
    is_posted = models.BooleanField(default=False)
    receipt_notes = models.CharField(max_length=255, default=None, blank=True, null=True)
    check_image_file_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    remittance_file_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse('receipt_detail', kwargs={'id':self.receipt_id})