from django.contrib import admin
from .models import AccountType, Account, TransactionSource, TransactionType

admin.site.register(AccountType)
admin.site.register(Account)
admin.site.register(TransactionSource)
admin.site.register(TransactionType)