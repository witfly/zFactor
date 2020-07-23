from django import forms
from .models import DisbursementRequest, RequestType
from client.models import Client, FundingAccount



class DisbursementRequestForm(forms.ModelForm):
    request_type = forms.ModelChoiceField(queryset=RequestType.objects.all(), initial=0, required=False)
    funding_account = forms.ModelChoiceField(queryset=FundingAccount.objects.all(), initial=0, required=False)
    client = forms.ModelChoiceField(queryset=Client.objects.all(), initial=0, required=False)
    amount = forms.DecimalField()   
    date_requested = forms.DateTimeField()
    reference_number = forms.CharField()
    check_number = forms.CharField()
    check_date = forms.DateTimeField()
    is_granted = forms.BooleanField() 
    is_cleared = forms.BooleanField() 
    notes = forms.CharField()    

    
    class Meta:
        model = DisbursementRequest
        fields = {
            'request_type',
            'funding_account',
            'client',
            'amount',  
            'reference_number',
            'check_number',
            'check_date',
            'is_granted', 
            'is_cleared', 
            'notes'

        }
