from django.contrib import admin
from . models import Operation, Cipher, Page, CryptodenUser

admin.site.register(Operation)
admin.site.register(Cipher)
admin.site.register(Page)
admin.site.register(CryptodenUser)
