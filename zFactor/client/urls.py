from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.ClientListView.as_view(), name = 'client_list'),
    # path('', views.list, name = 'list'),
    path('create', views.ClientCreateView.as_view(), name = 'new_client'),
    path('detail/<int:id>', views.ClientDetailView.as_view(), name = 'client_detail'),
    path('update/<int:id>', views.ClientUpdateView.as_view(), name = 'client_update'),
    path('delete/<int:id>', views.ClientDeleteView.as_view(), name = 'delete_client'),
    
    path('terms', views.TermsListView.as_view(), name = 'terms_list'),
    path('terms/create', views.TermsCreateView.as_view(), name = 'terms_new'),
    path('terms/detail/<int:id>', views.TermsDetailView.as_view(), name = 'terms_detail'),
    path('terms/update/<int:id>', views.TermsUpdateView.as_view(), name = 'terms_update'),
    path('terms/delete/<int:id>', views.TermsDeleteView.as_view(), name = 'terms_delete'),
    
    
    path('sales_broker', views.SalesBrokerListView.as_view(), name = 'sales_broker_list'),
    path('sales_broker/create', views.SalesBrokerCreateView.as_view(), name = 'sales_broker_new'),
    path('sales_broker/detail/<int:id>', views.SalesBrokerDetailView.as_view(), name = 'sales_broker_detail'),
    path('sales_broker/update/<int:id>', views.SalesBrokerUpdateView.as_view(), name = 'sales_broker_update'),
    path('sales_broker/delete/<int:id>', views.SalesBrokerDeleteView.as_view(), name = 'sales_broker_delete'),
    
    path('contact_account', views.ContactAccountListView.as_view(), name = 'contact_account_list'),
    path('contact_account/create', views.ContactAccountCreateView.as_view(), name = 'contact_account_new'),
    path('contact_account/detail/<int:id>', views.ContactAccountDetailView.as_view(), name = 'contact_account_detail'),
    path('contact_account/update/<int:id>', views.ContactAccountUpdateView.as_view(), name = 'contact_account_update'),
    path('contact_account/delete/<int:id>', views.ContactAccountDeleteView.as_view(), name = 'contact_account_delete'),
    
    path('client_contact', views.ClientContactListView.as_view(), name = 'client_contact_list'),
    path('client_contact/create', views.ClientContactCreateView.as_view(), name = 'client_contact_new'),
    path('client_contact/detail/<int:id>', views.ClientContactDetailView.as_view(), name = 'client_contact_detail'),
    path('client_contact/update/<int:id>', views.ClientContactUpdateView.as_view(), name = 'client_contact_update'),
    path('client_contact/delete/<int:id>', views.ClientContactDeleteView.as_view(), name = 'client_contact_delete'),
    
    path('funding_account', views.FundingAccountListView.as_view(), name = 'funding_account_list'),
    path('funding_account/create', views.FundingAccountCreateView.as_view(), name = 'funding_account_new'),
    path('funding_account/detail/<int:id>', views.FundingAccountDetailView.as_view(), name = 'funding_account_detail'),
    path('funding_account/update/<int:id>', views.FundingAccountUpdateView.as_view(), name = 'funding_account_update'),
    path('funding_account/delete/<int:id>', views.FundingAccountDeleteView.as_view(), name = 'funding_account_delete'),
    
    path('client_note', views.ClientNoteListView.as_view(), name = 'client_note_list'),
    path('client_note/create', views.ClientNoteCreateView.as_view(), name = 'client_note_new'),
    path('client_note/detail/<int:id>', views.ClientNoteDetailView.as_view(), name = 'client_note_detail'),
    path('client_note/update/<int:id>', views.ClientNoteUpdateView.as_view(), name = 'client_note_update'),
    path('client_note/delete/<int:id>', views.ClientNoteDeleteView.as_view(), name = 'client_note_delete'),
    
    path('client_document', views.ClientDocumentListView.as_view(), name = 'client_document_list'),
    path('client_document/create', views.ClientDocumentCreateView.as_view(), name = 'client_document_new'),
    path('client_document/detail/<int:id>', views.ClientDocumentDetailView.as_view(), name = 'client_document_detail'),
    path('client_document/update/<int:id>', views.ClientDocumentUpdateView.as_view(), name = 'client_document_update'),
    path('client_document/delete/<int:id>', views.ClientDocumentDeleteView.as_view(), name = 'client_document_delete'),
    
    path('bucket_rate', views.BucketRateListView.as_view(), name = 'bucket_rate_list'),
    path('bucket_rate/create', views.BucketRateCreateView.as_view(), name = 'bucket_rate_new'),
    path('bucket_rate/detail/<int:id>', views.BucketRateDetailView.as_view(), name = 'bucket_rate_detail'),
    path('bucket_rate/update/<int:id>', views.BucketRateUpdateView.as_view(), name = 'bucket_rate_update'),
    path('bucket_rate/delete/<int:id>', views.BucketRateDeleteView.as_view(), name = 'bucket_rate_delete')

]

