from django.shortcuts import render
from django.http import HttpResponse
from documents.models import inbox_documents, send_documents
from documents.buisnesLogic.test import search
from django.views.decorators.csrf import csrf_exempt
from documents.forms import choose_file_form 
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect

import sys
sys.path.append(r'/home/dariacross/Загрузки/pycades_0.1.44290/build/')
import pycades


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
        # print(search()[0])
        # dictreq = dict(request.POST.get('city'))
        # with open('files/hui.txt', 'a') as f:
        #     f.write('aaaa\n')
        # print(request.POST.get('city'))

        user_output = request.POST.get('user_output')
        context = {
                        "title": 'Входящие',
                        'inbox_docs': inbox_documents.objects.all(),
                        'prints0': search()[0], 
                        'prints1': search()[1],
                        'prints2': search()[2],
                        'prints3': search()[3],
                        'prints4': search()[4],           
                        'prints5': search()[5],
                        'prints6': search()[6],
                        'user_output': user_output,
                        }
        
        if user_output is None:
            print('QivivTop')
            # for i in range(len(search()[0])):

        else:

        # return HttpResponse('OK', status=200)

            user_output = int(request.POST.get('user_output'))
            print(user_output)

            store = pycades.Store()
            store.Open(pycades.CADESCOM_CONTAINER_STORE, pycades.CAPICOM_MY_STORE, pycades.CAPICOM_STORE_OPEN_MAXIMUM_ALLOWED)
            certs = store.Certificates
            
            signer = pycades.Signer()
            signer.Certificate = certs.Item(user_output)
            signer.CheckCertificate = True

            signedData = pycades.SignedData()
            signedData.Content = "Тестовые данные для подписания"
            signature = signedData.SignCades(signer, pycades.CADESCOM_CADES_BES)

            print("--Подпись--")
            print(signature)
            print("----")
            print('len of signature = ', len(signature))


            print('Проверка электронной подписи \n')
            _signedData = pycades.SignedData()
            _signedData.VerifyCades(signature, pycades.CADESCOM_CADES_BES)
            print('Успешная проверка')


        return render(request, 'documents/table.html', context=context)
    

    elif request.method == "GET":
        return HttpResponse('NE OK', status=200)


def choose(request):
    if request.method == 'POST':
        form = choose_file_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Файл успешно загружен')
            return HttpResponseRedirect(reverse('login'))
        else:
            print(form.errors)
    else:
        form = choose_file_form()
    context = {'form': form}
    return render(request, 'index', context)
