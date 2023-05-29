from django.shortcuts import render
from django.http import HttpResponse
from documents.models import inbox_documents, send_documents
from documents.buisnesLogic.test import funcstest
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return render(request, 'documents/index.html')

def table(request):
    print(request.user)
    context = {
        "title" : 'Входящие',
        'inbox_docs' : inbox_documents.objects.all(),
    }

    return render(request, 'documents/table.html', context=context)

@csrf_exempt
def podpis(request):
    if request.method == "POST":
        print(funcstest())
        dictreq = dict(request.POST)
        with open('files/hui.txt', 'a') as f:
            f.write('aaaa\n')
        context = {
            "title": 'Входящие',
            'inbox_docs': inbox_documents.objects.all(),
            'prints': funcstest(),
        }

        # return HttpResponse('OK', status=200)
        return render(request, 'documents/table.html', context=context)
    elif request.method == "GET":
        return HttpResponse('NE OK', status=200)