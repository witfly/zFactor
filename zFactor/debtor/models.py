from django.db import models
from django.urls import reverse
from soft_delete_it.models import SoftDeleteModel


class InvoiceDeliveryOption(SoftDeleteModel):
    option_id = models.AutoField(auto_created=True, primary_key=True)
    option_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    option_description = models.CharField(max_length=255, default=None, blank=True, null=True)
    
class Status(SoftDeleteModel):
    status_id = models.AutoField(auto_created=True, primary_key=True)
    status_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    status_description = models.CharField(max_length=255, default=None, blank=True, null=True)
    
    def __str__(self):
        return self.status_name

class Debtor(SoftDeleteModel):
    debtor_id = models.AutoField(auto_created=True, primary_key=True)
    parent = models.ForeignKey('self', default=None, blank=True, null=True, on_delete = models.SET_NULL)
    name = models.CharField(max_length=255)
    status = models.ForeignKey(Status,default=None, blank=True, null=True, on_delete = models.SET_NULL)
    docket = models.CharField(max_length=50, default=None, blank=True, null=True)
    dot_number = models.CharField(max_length=50, default=None, blank=True, null=True)
    business_phone = models.CharField(max_length=50, default=None, blank=True, null=True)
    business_fax = models.CharField(max_length=50, default=None, blank=True, null=True)
    business_email = models.EmailField(default=None, blank=True, null=True)
    fax_noa = models.CharField(max_length=50, default=None, blank=True, null=True)
    fax_statement = models.CharField(max_length=50, default=None, blank=True, null=True)
    fax_invoice = models.CharField(max_length=50, default=None, blank=True, null=True)
    email_noa = models.EmailField(default=None, blank=True, null=True)
    email_invoice = models.EmailField(default=None, blank=True, null=True)
    email_statement = models.EmailField(default=None, blank=True, null=True)
    email_subject = models.CharField(max_length=255, default=None, blank=True, null=True)
    invoice_delivery_option = models.ForeignKey(InvoiceDeliveryOption, default=None, blank=True, null=True, on_delete = models.SET_NULL)
    originals_required = models.BooleanField(default=False)
    credit_limit = models.DecimalField(decimal_places =2, max_digits = 10)
    credit_score = models.DecimalField(decimal_places =2, max_digits = 10)
    invoice_upload_website = models.CharField(max_length=255, default=None, blank=True, null=True)
    invoice_upload_user = models.CharField(max_length=255, default=None, blank=True, null=True)
    invoice_upload_password = models.CharField(max_length=255, default=None, blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse('debtor_detail', kwargs={'id':self.debtor_id})
    def __str__(self):
        return self.name
    
class DebtorNote(SoftDeleteModel):
    note_id = models.AutoField(auto_created=True, primary_key=True),
    debtor = models.ForeignKey(Debtor, related_name='debtor_memo', on_delete = models.CASCADE)
    debtor_note = models.CharField(max_length = 255)
    is_alert = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    show_client = models.BooleanField(default=False)
    
class ContactRole(SoftDeleteModel): # Owner, Employee, Accounts_Payable, Invoice_Verification,
    contact_role_id = models.AutoField(auto_created=True, primary_key=True)
    role_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    role_description = models.CharField(max_length=255, default=None, blank=True, null=True)
    def __str__(self):
        return self.role_name
    
class Contact(SoftDeleteModel):
    contact_id = models.AutoField(auto_created=True, primary_key=True)
    first_name = models.CharField(max_length=100, default=None, blank=True, null=True)
    middle_name = models.CharField(max_length=100, default=None, blank=True, null=True)
    last_name = models.CharField(max_length=100, default=None, blank=True, null=True)
    address_1 = models.CharField(max_length=100, default=None, blank=True, null=True)
    address_2 = models.CharField(max_length=100, default=None, blank=True, null=True)
    city  = models.CharField(max_length=100, default=None, blank=True, null=True)
    state = models.CharField(max_length=100, default=None, blank=True, null=True)
    country = models.CharField(max_length=100, default=None, blank=True, null=True)
    phone = models.CharField(max_length=100, default=None, blank=True, null=True)
    cell_phone = models.CharField(max_length=100, default=None, blank=True, null=True)
    email = models.EmailField(default=None, blank=True, null=True)
    is_active = models.BooleanField(default = True)
    contact_role = models.ForeignKey(ContactRole,  default=None, blank=True, null=True, on_delete=models.SET_NULL)
    portal_access_login = models.CharField(max_length=255, default=None, blank=True, null=True)
    portal_access_password = models.CharField(max_length=255, default=None, blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse('debtor_contact_detail', kwargs={'id': self.contact_id})
    
