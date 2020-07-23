from django.contrib import admin
from .models import Status, InvoiceDeliveryOption, ContactRole

admin.site.register(Status)
admin.site.register(InvoiceDeliveryOption)
admin.site.register(ContactRole)
