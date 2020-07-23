from django.db import models
from soft_delete_it.models import SoftDeleteModel
from invoice.models import Invoice

class DebtorResponse(SoftDeleteModel):
    debtor_response_id = models.AutoField(auto_created=True, primary_key=True)
    debtor_response = models.CharField(max_length=50)
    response_description = models.CharField(max_length=255, default=None, blank=True, null=True)

class CollectionNote(SoftDeleteModel): 
    collection_note_id = models.AutoField(auto_created=True, primary_key=True)
    debtor_response = models.ForeignKey(DebtorResponse, on_delete=models.PROTECT)
    note = models.CharField(max_length=255, default=None, blank=True, null=True)
    payment_date = models.DateTimeField()
    

class InvoiceCollectionNote(SoftDeleteModel):
    invoice_collection_note_id = models.AutoField(auto_created=True, primary_key=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    collection_note = models.ForeignKey(CollectionNote,on_delete=models.CASCADE)