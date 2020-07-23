from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.DisbursementRequestListView.as_view(), name = 'disbursement_request_list'),
    path('create', views.DisbursementRequestCreateView.as_view(), name = 'disbursement_request_new'),
    path('detail/<int:id>', views.DisbursementRequestDetailView.as_view(), name = 'disbursement_request_detail'),
    path('update/<int:id>', views.DisbursementRequestUpdateView.as_view(), name = 'disbursement_request_update'),
    path('delete/<int:id>', views.DisbursementRequestDeleteView.as_view(), name = 'disbursement_request_delete'),
    
    
]