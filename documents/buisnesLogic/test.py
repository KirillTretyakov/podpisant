import sys
sys.path.append(r'/home/dariacross/Загрузки/pycades_0.1.44290/build/')
import pycades

def search():
    store = pycades.Store()
    store.Open(pycades.CADESCOM_CONTAINER_STORE, pycades.CAPICOM_MY_STORE, pycades.CAPICOM_STORE_OPEN_MAXIMUM_ALLOWED)
    certs = store.Certificates
    data_certs = int(certs.Count) 
    if certs.Count != 0:
        text_search = 'Найдено сертификатов: '
        text_search = text_search + str(certs.Count)
    else:
        text_search = 'Сертификаты не найдены'  
        
    number = []
    issuer = []
    serial_number = []
    subject = []
    date_from = []
    date_to = [] 

    for i in range(1, certs.Count + 1):
        signer = pycades.Signer()
        signer.Certificate = certs.Item(i)
        number.append(i)
        issuer.append(str(signer.Certificate.IssuerName))
        serial_number.append(str(signer.Certificate.SerialNumber))
        subject.append(str(signer.Certificate.SubjectName))
        date_from.append(str(signer.Certificate.ValidFromDate))
        date_to.append(str(signer.Certificate.ValidToDate))

    return text_search, number, issuer, serial_number, subject, date_from, date_to, data_certs



