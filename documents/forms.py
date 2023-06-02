from django import forms
from documents.models import inbox_documents

class choose_file_form(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'Наименование документа'}))
    
    number = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'Номер документа'}))
    
    date_document = forms.DateField(widget=forms.DateInput(attrs={
        'class':'form-control', 'placeholder':'Дата документа'}))
    
    date_send = forms.DateField(widget=forms.DateInput(attrs={
        'class':'form-control', 'placeholder':'Дата отправки'}))
    
    file = forms.FileField(widget=forms.FileInput(attrs={
        'class':'form-control', 'placeholder':'Файл для подписания'}))
    
    status = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'Статус документа'}))
    
    sender = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'Отправитель'}))

    class Meta:
        model = inbox_documents
        fields = ('name', 'number', 'date_document', 'date_send', 'file', 'status', 'sender')