from django import forms
from .models import (Client, 
                     Terms, 
                     SalesBroker, 
                     ContactAccount, 
                     ContactType, 
                     Contact,
                     FundingAccount, 
                     ClientNote, 
                     ClientDocument, 
                     DocumentCategory,
                     BucketRate)

class ClientForm(forms.ModelForm):
    client_name = forms.CharField()
    dba_name = forms.CharField()
    docket = forms.CharField()
    dot_number = forms.CharField()
    ein = forms.CharField()
    business_type = forms.CharField()
    is_broker = forms.BooleanField(required=False)
    business_start_date = forms.DateField()
    business_phone = forms.CharField()
    business_fax = forms.CharField()
    business_email = forms.EmailField()
    number_of_trucks = forms.IntegerField()
    account_manager = forms.CharField()
    hold_reserves = forms.BooleanField()
    credit_limit = forms.DecimalField()
    estimated_grp = forms.DecimalField()
    estimated_volume = forms.DecimalField()
    insurance_expiration_date = forms.DateField()
    ucc_filing_date = forms.DateField()
    
    class Meta:
        model = Client
        fields = {
            'client_name',     
            'dba_name', 
            'docket', 
            'dot_number', 
            'ein', 
            'business_type', 
            'is_broker', 
            'business_start_date', 
            'transaction_fee_rate_type',
            'business_phone', 
            'business_fax', 
            'business_email', 
            'number_of_trucks', 
            'primary_salesperson', 
            'secondary_salesperson', 
            'sales_broker',
            'credit_limit', 
            'estimated_grp', 
            'estimated_volume', 
            'insurance_expiration_date', 
            'ucc_filing_date' 
        }
        


class TermsForm(forms.ModelForm):
    description =forms.CharField()
    advance_percentage = forms.DecimalField()
    security_percentage = forms.DecimalField()
    invoice_fee = forms.DecimalField()
    flat_rate = forms.DecimalField()
    daily_rate = forms.DecimalField()
    express_processing_fee = forms.DecimalField()
    priority_processing_fee = forms.DecimalField()
    standard_processing_fee = forms.DecimalField()
    fuel_advance_percentage = forms.DecimalField()
    fuel_advance_fee_percentage = forms.DecimalField()
    fuel_advance_days = forms.IntegerField()
    over_advance_fee_percentage = forms.DecimalField()
    over_advance_days = forms.IntegerField()
    check_fee = forms.DecimalField()
    wire_fee = forms.DecimalField()
    transcheck_fee = forms.DecimalField()
    ach_fee = forms.DecimalField()
    fuel_card_fee = forms.DecimalField()
    carrier_quck_pay_fee = forms.DecimalField()
    paperwork_delivery_fee = forms.DecimalField()
    postage_fee = forms.DecimalField()
    release_days = forms.IntegerField()
    recourse_days = forms.IntegerField()
    
    class Meta:
        model = Terms
        fields = {
            'description',
            'advance_percentage',
            'security_percentage',
            'invoice_fee',
            'transaction_fee_rate_type',
            'flat_rate',
            'daily_rate',
            'express_processing_fee',
            'priority_processing_fee',
            'standard_processing_fee',
            'fuel_advance_percentage',
            'fuel_advance_fee_percentage',
            'fuel_advance_days',
            'over_advance_fee_percentage',
            'over_advance_days',
            'check_fee',
            'wire_fee',
            'transcheck_fee',
            'ach_fee',
            'fuel_card_fee',
            'carrier_quck_pay_fee',
            'paperwork_delivery_fee',
            'postage_fee',
            'release_days',
            'recourse_days'
        }
        
        
class SalesBrokerForm(forms.ModelForm):
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
    company_name = forms.CharField()
    
    class Meta:
        model = SalesBroker
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
            'company_name'
        }
        
class ContactAccountForm(forms.ModelForm):
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
    contact_type = forms.ModelChoiceField(queryset=ContactType.objects.all(), initial=0)
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    pin = forms.CharField()
    
    class Meta:
        model = ContactAccount
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
            'contact_type', 
            'login',
            'password',
            'pin',
        }
        
class ClientContactForm(forms.ModelForm):
    client = forms.ModelChoiceField(queryset=Client.objects.all(), initial=0)
    client_contact_account = forms.ModelChoiceField(queryset=ContactAccount.objects.all(), initial=0)
    is_active = forms.BooleanField(initial=True)
    can_move_money = forms.BooleanField(initial=False)
    
    class Meta:
        model = Contact
        fields = {
            'client',
            'client_contact_account',
            'is_active',
            'can_move_money'
        }
        
class FundingAccountForm(forms.ModelForm):
    client = forms.ModelChoiceField(queryset=Client.objects.all(), initial=0)
    vendor_name = forms.CharField()
    vendor_nick_name = forms.CharField()
    address_1 = forms.CharField()
    address_2 = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    zip = forms.CharField()
    country = forms.CharField()
    bank_name = forms.CharField()
    bank_routing_number = forms.CharField()
    bank_account_number = forms.CharField()
    bank_address_1 = forms.CharField()
    bank_address_2 = forms.CharField()
    bank_city = forms.CharField()
    bank_state = forms.CharField()
    bank_zip = forms.CharField()
    bank_country = forms.CharField()
    is_verified = forms.BooleanField()
    is_fuel_card = forms.BooleanField()
    wire_allowed = forms.BooleanField()
    ach_allowed = forms.BooleanField()
    check_allowed = forms.BooleanField()
    is_active = forms.BooleanField()

    
    class Meta:
        model = FundingAccount
        fields = {
            'client',
            'vendor_name',
            'vendor_nick_name',
            'address_1',
            'address_2',
            'city',
            'state',
            'zip',
            'country',
            'bank_name',
            'bank_routing_number',
            'bank_account_number',
            'bank_address_1',
            'bank_address_2',
            'bank_city',
            'bank_state',
            'bank_zip',
            'bank_country',
            'is_verified',
            'is_fuel_card',
            'wire_allowed',
            'ach_allowed',
            'check_allowed',
            'is_active'

        }
        
# Client Notes

class ClientNoteForm(forms.ModelForm):
    client = forms.ModelChoiceField(queryset=Client.objects.all(), initial=0)
    client_note = forms.CharField()
    is_alert = forms.BooleanField()
    is_active = forms.BooleanField()
    show_processing = forms.BooleanField()
    show_account_managers = forms.BooleanField()
    show_collections = forms.BooleanField()
    show_payments = forms.BooleanField()
    show_client = forms.BooleanField()

    
    class Meta:
        model = ClientNote
        fields = {
            'client',
            'client_note',
            'is_alert',
            'is_active',
            'show_processing',
            'show_account_managers',
            'show_collections',
            'show_payments',
            'show_client'

        }
        
# Client Document

class ClientDocumentForm(forms.ModelForm):
    client = forms.ModelChoiceField(queryset=Client.objects.all(), initial=0)
    document_category = forms.ModelChoiceField(queryset=DocumentCategory.objects.all(), initial=0)
    document_description = forms.CharField()
    date_created = forms.DateTimeField()
    is_active = forms.BooleanField()
    file_name = forms.CharField()
    file_extension = forms.CharField()
    file_size = forms.CharField()    

    
    class Meta:
        model = ClientDocument
        fields = {
            'client',
            'document_category',
            'document_description',
            'is_active',
            'file_name',
            'file_extension',
            'file_size'

        }
        
        
# Bucket rates


class BucketRateForm(forms.ModelForm):
    terms = forms.ModelChoiceField(queryset=Terms.objects.all(), initial=0)
    level = forms.IntegerField()
    min_days = forms.IntegerField()
    max_days = forms.IntegerField()
    percentage_rate = forms.DecimalField()   

    
    class Meta:
        model = BucketRate
        fields = {
            'terms',
            'level',
            'min_days',
            'max_days',
            'percentage_rate'

        }