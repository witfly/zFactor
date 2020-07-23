from django.db import models
from django.urls import reverse
from soft_delete_it.models import SoftDeleteModel
from invoice.models import Invoice



class InvoiceDeliveryOption(SoftDeleteModel): # Mail, Email, Fax, Upload,
    invoice_delivery_option_id = models.AutoField(auto_created=True, primary_key=True)
    option_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    option_description = models.CharField(max_length=255, default=None, blank=True, null=True)
    
    def __str__(self):
        return self.option_name

    
class InvoiceDeliveryTask(SoftDeleteModel):
    invoice_delivery_task_id = models.AutoField(auto_created=True, primary_key=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    invoice_delivery_option = models.ForeignKey(InvoiceDeliveryOption, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    is_delivered = models.BooleanField(default=False)
    date_delivered = models.DateTimeField(default=None, blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse('invoice_delivery_task_detail', kwargs={'id':self.invoice_delivery_task_id})