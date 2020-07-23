from django.db import models
from django.urls import reverse
from soft_delete_it.models import SoftDeleteModel
from client.models import Client,Terms
from debtor.models import Debtor


class NOA(SoftDeleteModel):
    noa_id = models.AutoField(auto_created=True, primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE)
    terms = models.ForeignKey(Terms, on_delete=models.PROTECT, default=None, null=True, blank=True)
    is_customized = models.BooleanField(default=False)
    is_debtor_notified = models.BooleanField(default=False)
    debtor_notification_date = models.DateTimeField(default=None, blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse('noa_detail', kwargs={'id':self.noa_id})
    
class PurchaseOption(SoftDeleteModel):
    purchase_option_id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    
class InvoiceStatus(SoftDeleteModel):
    invoice_status_id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Invoice(SoftDeleteModel):
    invoice_id = models.AutoField(auto_created=True, primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    debtor = models.ForeignKey(Debtor, on_delete=models.PROTECT)
    invoice_number = models.CharField(max_length=50, default=None, blank=True, null=True)
    load_number = models.CharField(max_length=255, default=None, blank=True, null=True)
    bol_number = models.CharField(max_length=50, default=None, blank=True, null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=11)
    is_fuel_advance = models.BooleanField(default=False)
    terms = models.ForeignKey(Terms, on_delete=models.PROTECT, default=None, null=True, blank=True)
    purchase_option = models.ForeignKey(PurchaseOption, on_delete=models.PROTECT)
    is_document_ready = models.BooleanField(default=False)
    status = models.ForeignKey(InvoiceStatus, on_delete=models.PROTECT)
    date_funded = models.DateTimeField(default=None, blank=True, null=True)
    date_due = models.DateTimeField(default=None, blank=True, null=True)
    is_on_hold = models.BooleanField(default=False)
    is_charged_back = models.BooleanField(default=False)
    job_number = models.CharField(max_length=50, default=None, blank=True, null=True)
    load_lable = models.CharField(max_length=50, default=None, blank=True, null=True)
    track_number = models.CharField(max_length=50, default=None, blank=True, null=True)
    pickup_date = models.DateTimeField(default=None, blank=True, null=True)
    pickup_address = models.CharField(max_length=255, default=None, blank=True, null=True)
    pickup_city = models.CharField(max_length=50, default=None, blank=True, null=True)
    pickup_state = models.CharField(max_length=50, default=None, blank=True, null=True)
    pickup_zip =  models.CharField(max_length=50, default=None, blank=True, null=True)
    delivery_date = models.DateTimeField(default=None, blank=True, null=True)
    delivery_address = models.CharField(max_length=255, default=None, blank=True, null=True)
    delivery_city = models.CharField(max_length=50, default=None, blank=True, null=True)
    delivery_state = models.CharField(max_length=50, default=None, blank=True, null=True)
    delivery_zip = models.CharField(max_length=50, default=None, blank=True, null=True)
    memo = models.CharField(max_length=255, default=None, blank=True, null=True)
    document_path = models.CharField(max_length=255, default=None, blank=True, null=True)
    document_file_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    noa = models.ForeignKey(NOA, on_delete=models.PROTECT)
    
    def get_absolute_url(self):
        return reverse('invoice_detail', kwargs={'id':self.invoice_id})
    
    
class LineItem(SoftDeleteModel): # Rate, Detention, Lamper fee, other...
    line_item_id = models.AutoField(auto_created=True, primary_key=True)
    line_item_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    line_item_description = models.CharField(max_length=255, default=None, blank=True, null=True)
    
    def __str__(self):
        return self.line_item_name
    

class InvoiceLineItems(SoftDeleteModel):
    invoice_line_item_id = models.AutoField(auto_created=True, primary_key=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT)
    line_item_id = models.ForeignKey(LineItem, on_delete=models.PROTECT)
    amount = models.DecimalField(decimal_places=2, max_digits=11)
    
    def get_absolute_url(self):
        return reverse('invoice_line_item_detail', kwargs={'id':self.invoice_line_item_id})
