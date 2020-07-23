from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import DisbursementRequestForm
from .models import DisbursementRequest

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)


class DisbursementRequestCreateView(CreateView):
    template_name = 'disbursement_request/create.html'
    form_class = DisbursementRequestForm
    queryset = DisbursementRequest.objects.all()
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    

class DisbursementRequestListView(ListView):
    template_name = 'disbursement_request/list.html'
    queryset = DisbursementRequest.objects.all()
    
class DisbursementRequestDetailView(DetailView):
    template_name = 'disbursement_request/detail.html'
    disbursement_request = DisbursementRequest.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(DisbursementRequest, request_id = id_)
    
class DisbursementRequestUpdateView(UpdateView):
    template_name = 'disbursement_request/create.html'
    form_class = DisbursementRequestForm
    queryset = DisbursementRequest.objects.all()
        
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(DisbursementRequest, request_id = id_)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class DisbursementRequestDeleteView(DeleteView):
    template_name = 'disbursement_request/delete.html'
    disbursement_request = DisbursementRequest.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(DisbursementRequest, request_id = id_)
    
    def get_success_url(self):
        return reverse('disbursement_request_list')