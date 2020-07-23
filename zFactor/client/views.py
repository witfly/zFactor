from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import (ClientForm, 
                    TermsForm,
                    SalesBrokerForm, 
                    ContactAccountForm, 
                    ClientContactForm, 
                    FundingAccountForm, 
                    ClientNoteForm,
                    ClientDocumentForm,
                    BucketRateForm)
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import (Client, 
                     Terms,
                     SalesBroker, 
                     ContactAccount, 
                     Contact, 
                     FundingAccount, 
                     ClientNote,
                     ClientDocument,
                     BucketRate)

class ClientCreateView(CreateView):
    template_name = 'client/create.html'
    form_class = ClientForm
    queryset = Client.objects.all()
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    

class ClientListView(ListView):
    template_name = 'client/list.html'
    queryset = Client.objects.all()
    
class ClientDetailView(DetailView):
    template_name = 'client/detail.html'
    client = Client.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Client, client_id = id_)
    
class ClientUpdateView(UpdateView):
    template_name = 'client/create.html'
    form_class = ClientForm
    queryset = Client.objects.all()
        
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Client, client_id = id_)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class ClientDeleteView(DeleteView):
    template_name = 'client/delete.html'
    client = Client.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Client, client_id = id_)
    
    def get_success_url(self):
        return reverse('client_list')
    
    
# Terms Views

   
class TermsCreateView(CreateView):
    template_name = 'terms/create.html'
    form_class = TermsForm
    queryset = Terms.objects.all()
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    

class TermsListView(ListView):
    template_name = 'terms/list.html'
    queryset = Terms.objects.all()
    
class TermsDetailView(DetailView):
    template_name = 'terms/detail.html'
    terms = Terms.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Terms, terms_id = id_)
    
class TermsUpdateView(UpdateView):
    template_name = 'terms/create.html'
    form_class = TermsForm
    queryset = Terms.objects.all()
        
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Terms, terms_id = id_)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class TermsDeleteView(DeleteView):
    template_name = 'terms/delete.html'
    terms = Terms.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Terms, terms_id = id_)
    
    def get_success_url(self):
        return reverse('terms_list')
    
# sales_broker

class SalesBrokerCreateView(CreateView):
    template_name = 'sales_broker/create.html'
    form_class = SalesBrokerForm
    queryset = SalesBroker.objects.all()
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    

class SalesBrokerListView(ListView):
    template_name = 'sales_broker/list.html'
    queryset = SalesBroker.objects.all()
    
class SalesBrokerDetailView(DetailView):
    template_name = 'sales_broker/detail.html'
    sales_broker = SalesBroker.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(SalesBroker, sales_broker_id = id_)
    
class SalesBrokerUpdateView(UpdateView):
    template_name = 'sales_broker/create.html'
    form_class = SalesBrokerForm
    queryset = SalesBroker.objects.all()
        
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(SalesBroker, sales_broker_id = id_)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class SalesBrokerDeleteView(DeleteView):
    template_name = 'sales_broker/delete.html'
    sales_broker = SalesBroker.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(SalesBroker, sales_broker_id = id_)
    
    def get_success_url(self):
        return reverse('sales_broker_list')


# contact account

class ContactAccountCreateView(CreateView):
    template_name = 'contact_account/create.html'
    form_class = ContactAccountForm
    queryset = ContactAccount.objects.all()
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    

class ContactAccountListView(ListView):
    template_name = 'contact_account/list.html'
    queryset = ContactAccount.objects.all()
    
class ContactAccountDetailView(DetailView):
    template_name = 'contact_account/detail.html'
    contact_account = ContactAccount.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(ContactAccount, contact_account_id = id_)
    
class ContactAccountUpdateView(UpdateView):
    template_name = 'contact_account/create.html'
    form_class = ContactAccountForm
    queryset = ContactAccount.objects.all()
        
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(ContactAccount, contact_account_id = id_)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class ContactAccountDeleteView(DeleteView):
    template_name = 'contact_account/delete.html'
    contact_account = ContactAccount.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(ContactAccount, contact_account_id = id_)
    
    def get_success_url(self):
        return reverse('contact_account_list')
    
    
# Client contact

class ClientContactCreateView(CreateView):
    template_name = 'client_contact/create.html'
    form_class = ClientContactForm
    queryset = Contact.objects.all()
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    

class ClientContactListView(ListView):
    template_name = 'client_contact/list.html'
    queryset = Contact.objects.all()
    
class ClientContactDetailView(DetailView):
    template_name = 'client_contact/detail.html'
    client_contact = Contact.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Contact, account_id = id_)
    
class ClientContactUpdateView(UpdateView):
    template_name = 'client_contact/create.html'
    form_class = ClientContactForm
    queryset = Contact.objects.all()
        
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Contact, contact_id = id_)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class ClientContactDeleteView(DeleteView):
    template_name = 'client_contact/delete.html'
    client_contact = Contact.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Contact, contact_id = id_)
    
    def get_success_url(self):
        return reverse('client_contact_list')


# Funding Accounts

class FundingAccountCreateView(CreateView):
    template_name = 'funding_account/create.html'
    form_class = FundingAccountForm
    queryset = FundingAccount.objects.all()
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    

class FundingAccountListView(ListView):
    template_name = 'funding_account/list.html'
    queryset = FundingAccount.objects.all()
    
class FundingAccountDetailView(DetailView):
    template_name = 'funding_account/detail.html'
    funding_account = FundingAccount.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(FundingAccount, funding_account_id = id_)
    
class FundingAccountUpdateView(UpdateView):
    template_name = 'funding_account/create.html'
    form_class = FundingAccountForm
    queryset = FundingAccount.objects.all()
        
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(FundingAccount, funding_account_id = id_)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class FundingAccountDeleteView(DeleteView):
    template_name = 'funding_account/delete.html'
    funding_account = FundingAccount.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(FundingAccount, funding_account_id = id_)
    
    def get_success_url(self):
        return reverse('funding_account_list')



#Client Notes


class ClientNoteCreateView(CreateView):
    template_name = 'client_note/create.html'
    form_class = ClientNoteForm
    queryset = ClientNote.objects.all()
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    

class ClientNoteListView(ListView):
    template_name = 'client_note/list.html'
    queryset = ClientNote.objects.all()
    
class ClientNoteDetailView(DetailView):
    template_name = 'client_note/detail.html'
    client_note = FundingAccount.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(FundingAccount, client_note_id = id_)
    
class ClientNoteUpdateView(UpdateView):
    template_name = 'client_note/create.html'
    form_class = ClientNoteForm
    queryset = ClientNote.objects.all()
        
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(ClientNote, client_note_id = id_)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class ClientNoteDeleteView(DeleteView):
    template_name = 'client_note/delete.html'
    client_note = ClientNote.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(ClientNote, client_note_id = id_)
    
    def get_success_url(self):
        return reverse('client_note_list')
    
    
    
# Client Documents


class ClientDocumentCreateView(CreateView):
    template_name = 'client_document/create.html'
    form_class = ClientDocumentForm
    queryset = ClientDocument.objects.all()
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    

class ClientDocumentListView(ListView):
    template_name = 'client_document/list.html'
    queryset = ClientDocument.objects.all()
    
class ClientDocumentDetailView(DetailView):
    template_name = 'client_document/detail.html'
    client_document = ClientDocument.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(ClientDocument, client_document_id = id_)
    
class ClientDocumentUpdateView(UpdateView):
    template_name = 'client_document/create.html'
    form_class = ClientDocumentForm
    queryset = ClientDocument.objects.all()
        
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(ClientDocument, client_document_id = id_)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class ClientDocumentDeleteView(DeleteView):
    template_name = 'client_document/delete.html'
    client_document = ClientDocument.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(ClientDocument, client_document_id = id_)
    
    def get_success_url(self):
        return reverse('client_document_list')
    
    
# Bucket Rates


class BucketRateCreateView(CreateView):
    template_name = 'bucket_rate/create.html'
    form_class = BucketRateForm
    queryset = BucketRate.objects.all()
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    

class BucketRateListView(ListView):
    template_name = 'bucket_rate/list.html'
    queryset = BucketRate.objects.all()
    
class BucketRateDetailView(DetailView):
    template_name = 'bucket_rate/detail.html'
    bucket_rate = BucketRate.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(BucketRate, bucket_rate_id = id_)
    
class BucketRateUpdateView(UpdateView):
    template_name = 'bucket_rate/create.html'
    form_class = BucketRateForm
    queryset = BucketRate.objects.all()
        
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(BucketRate, bucket_rate_id = id_)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class BucketRateDeleteView(DeleteView):
    template_name = 'bucket_rate/delete.html'
    bucket_rate = BucketRate.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(BucketRate, bucket_rate_id = id_)
    
    def get_success_url(self):
        return reverse('bucket_rate_list')
 
 

""" 
def list_view(request, *args, **kwargs):
    client_list = Client.objects.all()
    context = {
        'client_list': client_list
    }
    return render(request, 'client/list.html', context)

def create_view(request):
    form = ClientForm()
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            form = ClientForm()    
    context = {
        'form': form
    }
    
    return render(request, 'client/create.html', context)

def detail_view(request, id):
    obj = get_object_or_404(Client, client_id=id)
    form = ClientForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    
    context = {
        'form': form
    }
    return render(request, 'client/detail.html', context)

def delete_view(request, id):
    obj = get_object_or_404(Client, client_id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('client/list.html')
    
    context = {
        'object': obj
    }
    return render(request, 'client/delete.html', context) """

