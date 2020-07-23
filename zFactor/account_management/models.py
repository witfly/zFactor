from django.db import models
from django.urls import reverse
from soft_delete_it.models import SoftDeleteModel
from client.models import Client, Terms


class OverAdvance(SoftDeleteModel):
    over_advance_id = models.AutoField(auto_created=True, primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    term = models.ForeignKey(Terms, on_delete=models.PROTECT)
    over_advance_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    due_date = models.DateTimeField(default=None, blank=True, null=True)
    is_closed = models.BooleanField(default=False)
    date_closed = models.DateTimeField(default=None, blank=True, null=True)
    is_extended = models.BooleanField(default=False)
    
    def get_absolute_url(self):
        return reverse('over_advance_detail', kwargs={'id': self.over_advance_id})
    

class OverAdvanceNote(SoftDeleteModel):
    over_advance_note_id = models.AutoField(auto_created=True, primary_key=True)
    over_advance = models.ForeignKey(OverAdvance, on_delete=models.CASCADE)
    note = models.CharField(max_length=255)
    
    def get_absolute_url(self):
        return reverse('over_advance_note_detail', kwargs={'id': self.over_advance_note_id})


class MiscChargeType(SoftDeleteModel):
    misc_charge_type_id = models.AutoField(auto_created=True, primary_key=True)
    charge_name = models.CharField(max_length=50)
    charge_description = models.CharField(max_length=255, default=None, blank=True, null=True)
    
    def __str__(self):
        return self.charge_name

class MiscCharge(SoftDeleteModel):
    misc_charge_id = models.AutoField(auto_created=True, primary_key=True)
    misc_charge_type = models.ForeignKey(MiscChargeType, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    note = models.CharField(max_length=255, default=None, null=True, blank=True)
    charge_date = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse('misc_charge_detail', kwargs={'id': self.misc_charge_id})