from django import forms
from .models import Debtor, Contact, Status, InvoiceDeliveryOption, ContactRole, DebtorNote



class DebtorForm(forms.ModelForm):
    parent = forms.ModelChoiceField(queryset=Debtor.objects.all(), initial=0, required=False)
    name = forms.CharField()
    status = forms.ModelChoiceField(queryset=Status.objects.all(), initial=0)
    docket = forms.CharField()
    dot_number = forms.CharField()
    business_phone = forms.CharField()
    business_fax = forms.CharField()
    business_email = forms.EmailField()
    fax_noa = forms.CharField()
    fax_statement = forms.CharField()
    fax_invoice = forms.CharField()
    email_noa = forms.EmailField()
    email_invoice = forms.EmailField()
    email_statement = forms.EmailField()
    email_subject = forms.CharField()
    invoice_delivery_option = forms.ModelChoiceField(queryset=InvoiceDeliveryOption.objects.all(), initial=0)
    originals_required = forms.BooleanField()
    credit_limit = forms.DecimalField()
    credit_score = forms.DecimalField()
    invoice_upload_website = forms.CharField()
    invoice_upload_user = forms.CharField()
    invoice_upload_password = forms.CharField()

    
    class Meta:
        model = Debtor
        fields = {
            'parent' ,
            'name',
            'status',
            'docket',
            'dot_number',
            'business_phone',
            'business_fax',
            'business_email',
            'fax_noa',
            'fax_statement',
            'fax_invoice',
            'email_noa',
            'email_invoice',
            'email_statement',
            'email_subject',
            'invoice_delivery_option',
            'originals_required',
            'credit_limit',
            'credit_score',
            'invoice_upload_website',
            'invoice_upload_user',
            'invoice_upload_password'

        }


class DebtorContactForm(forms.ModelForm):
    first_name = forms.CharField()
    middle_name = forms.CharField()
    last_name = forms.CharField()
    address_1 = forms.CharField()
    address_2 = forms.CharField()
    city  = forms.CharField()
    state = forms.CharField()
    country = forms.CharField()
    phone = forms.CharField()
    cell_phone = forms.CharField()
    email = forms.EmailField()
    is_active = forms.BooleanField()
    contact_role = forms.ModelChoiceField(queryset=ContactRole.objects.all(), initial=0)
    portal_access_login = forms.CharField()
    portal_access_password = forms.CharField()
    
    class Meta:
        model = Contact
        fields = {
            'first_name',
            'middle_name',
            'last_name',
            'address_1',
            'address_2',
            'city',
            'state',
            'country',
            'phone',
            'cell_phone',
            'email',
            'is_active',
            'contact_role',
            'portal_access_login',
            'portal_access_password'
        }
        
        
class DebtorNoteForm(forms.ModelForm):
    debtor = forms.ModelChoiceField(queryset=Debtor.objects.all(), initial=0)
    debtor_note = forms.CharField()
    is_alert = forms.BooleanField()
    is_active = forms.BooleanField()
    show_client = forms.BooleanField()

    
    class Meta:
        model = Contact
        fields = {
            'debtor',
            'debtor_note',
            'is_alert',
            'is_active',
            'show_client'
        }