from django.contrib import admin
from .models import InvoiceStatus, PurchaseOption, LineItem

admin.site.register(InvoiceStatus)
admin.site.register(PurchaseOption)
admin.site.register(LineItem)
