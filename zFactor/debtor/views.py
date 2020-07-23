from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import DebtorForm, DebtorContactForm, DebtorNoteForm
from .models import Debtor, Contact, DebtorNote

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

class DebtorCreateView(CreateView):
    template_name = 'debtor/create.html'
    form_class = DebtorForm
    queryset = Debtor.objects.all()
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    

class DebtorListView(ListView):
    template_name = 'debtor/list.html'
    queryset = Debtor.objects.all()
    
class DebtorDetailView(DetailView):
    template_name = 'debtor/detail.html'
    debtor = Debtor.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Debtor, debtor_id = id_)
    
class DebtorUpdateView(UpdateView):
    template_name = 'debtor/create.html'
    form_class = DebtorForm
    queryset = Debtor.objects.all()
        
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Debtor, debtor_id = id_)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class DebtorDeleteView(DeleteView):
    template_name = 'debtor/delete.html'
    debtor = Debtor.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Debtor, debtor_id = id_)
    
    def get_success_url(self):
        return reverse('debtor_list')
    

# Debtor Contact

class DebtorContactCreateView(CreateView):
    template_name = 'debtor_contact/create.html'
    form_class = DebtorContactForm
    queryset = Contact.objects.all()
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    

class DebtorContactListView(ListView):
    template_name = 'debtor_contact/list.html'
    queryset = Contact.objects.all()
    
class DebtorContactDetailView(DetailView):
    template_name = 'debtor_contact/detail.html'
    debtor_contact = Contact.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Contact, contact_id = id_)
    
class DebtorContactUpdateView(UpdateView):
    template_name = 'debtor_contact/create.html'
    form_class = DebtorContactForm
    queryset = Contact.objects.all()
        
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Contact, contact_id = id_)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class DebtorContactDeleteView(DeleteView):
    template_name = 'debtor_contact/delete.html'
    debtor_contact = Contact.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Contact, contact_id = id_)
    
    def get_success_url(self):
        return reverse('debtor_contact_list')
    
    
    
# Debtor Note

class DebtorNoteCreateView(CreateView):
    template_name = 'debtor_note/create.html'
    form_class = DebtorNoteForm
    queryset = DebtorNote.objects.all()
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    

class DebtorNoteListView(ListView):
    template_name = 'debtor_note/list.html'
    queryset = DebtorNote.objects.all()
    
class DebtorNoteDetailView(DetailView):
    template_name = 'debtor_note/detail.html'
    debtor_note = DebtorNote.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(DebtorNote, note_id = id_)
    
class DebtorNoteUpdateView(UpdateView):
    template_name = 'debtor_note/create.html'
    form_class = DebtorNoteForm
    queryset = DebtorNote.objects.all()
        
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Contact, note_id = id_)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class DebtorNoteDeleteView(DeleteView):
    template_name = 'debtor_note/delete.html'
    debtor_note = Contact.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(DebtorNote, note_id = id_)
    
    def get_success_url(self):
        return reverse('debtor_note_list')
    