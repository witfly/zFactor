from django.db import models
from django.urls import reverse
from soft_delete_it.models import SoftDeleteModel
from invoice.models import Invoice

# Create your models here.


class InvoiceHoldReason(SoftDeleteModel): # Mail, Email, Fax, Upload,
    invoice_hold_reason_id = models.AutoField(auto_created=True, primary_key=True)
    hold_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    hold_description = models.CharField(max_length=255, default=None, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.hold_name
    
class ProcessingNote(SoftDeleteModel):
    note_id = models.AutoField(auto_created=True, primary_key=True),
    invoice = models.ForeignKey(Invoice, related_name='processing_note', on_delete = models.CASCADE)
    hold_reason = models.ForeignKey(InvoiceHoldReason, default=None, blank=True, null=True,on_delete=models.PROTECT)
    note = models.CharField(max_length = 255)
    is_alert = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    show_client = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse('processing_note_detail', kwargs={'id':self.note_id})