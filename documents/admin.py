from django.contrib import admin

# Register your models here.
from documents.models import inbox_documents, send_documents

admin.site.register(inbox_documents)
admin.site.register(send_documents)