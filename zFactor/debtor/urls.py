from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.DebtorListView.as_view(), name = 'debtor_list'),
    path('create', views.DebtorCreateView.as_view(), name = 'debtor_new'),
    path('detail/<int:id>', views.DebtorDetailView.as_view(), name = 'debtor_detail'),
    path('update/<int:id>', views.DebtorUpdateView.as_view(), name = 'debtor_update'),
    path('delete/<int:id>', views.DebtorDeleteView.as_view(), name = 'debtor_delete'),
    
    path('contact', views.DebtorContactListView.as_view(), name = 'debtor_contact_list'),
    path('contact/create', views.DebtorContactCreateView.as_view(), name = 'debtor_contact_new'),
    path('contact/detail/<int:id>', views.DebtorContactDetailView.as_view(), name = 'debtor_contact_detail'),
    path('contact/update/<int:id>', views.DebtorContactUpdateView.as_view(), name = 'debtor_contact_update'),
    path('contact/delete/<int:id>', views.DebtorContactDeleteView.as_view(), name = 'debtor_contact_delete'),
    
    path('debtor_note', views.DebtorNoteListView.as_view(), name = 'debtor_note_list'),
    path('debtor_note/create', views.DebtorNoteCreateView.as_view(), name = 'debtor_note_new'),
    path('debtor_note/detail/<int:id>', views.DebtorNoteDetailView.as_view(), name = 'debtor_note_detail'),
    path('debtor_note/update/<int:id>', views.DebtorNoteUpdateView.as_view(), name = 'debtor_note_update'),
    path('debtor_note/delete/<int:id>', views.DebtorNoteDeleteView.as_view(), name = 'debtor_note_delete'),
    
]