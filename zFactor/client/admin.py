from django.contrib import admin

from .models import ContactType, TransactionFeeRateType, DocumentCategory

admin.site.register(TransactionFeeRateType)
admin.site.register(ContactType)
admin.site.register(DocumentCategory)

