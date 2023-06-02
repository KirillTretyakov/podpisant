from django.db import models
from django import forms

# Create your models here.
# TextField()
#
class inbox_documents(models.Model):
    name = models.CharField(max_length=128)
    number = models.CharField(max_length=128, null=True, blank=True)
    date_document = models.DateField(null=True, blank=True)
    date_send = models.DateField()
    file = models.FileField(upload_to='files/', null=True)
    status = models.CharField(max_length=15)
    sender = models.CharField(max_length=100)

    def __str__(self):
        return f'Имя файла: {self.name} | Статус: {self.status} | Дата отправки: {self.date_send}'

class send_documents(models.Model):
    name = models.CharField(max_length=128)
    number = models.CharField(max_length=128, null=True, blank=True)
    date_document = models.DateField(null=True, blank=True)
    date_send = models.DateField()
    file = models.FileField(upload_to='files/', null=True)
    status = models.CharField(max_length=15)
    inboxer = models.CharField(max_length=100)

    def __str__(self):
        return f'Имя файла: {self.name} | Статус: {self.status} | Дата отправки: {self.date_send}'

