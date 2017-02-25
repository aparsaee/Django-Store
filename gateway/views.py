# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from suds.client import Client
# Create your views here.
MMERCHANT_ID = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'  # Required
ZARINPAL_WEBSERVICE = 'https://www.zarinpal.com/pg/services/WebGate/wsdl'  # Required
amount = 1000  # Amount will be based on Toman  Required
description = u'توضیحات تراکنش تستی'  # Required
email = 'user@userurl.ir'  # Optional
mobile = '09123456789'  # Optional


def send_request(request):
    client = Client(ZARINPAL_WEBSERVICE)
    result = client.service.PaymentRequest(MMERCHANT_ID,
                                           amount,
                                           description,
                                           email,
                                           mobile,
                                           str('verify'))
    if result.Status == 100:
        return HttpResponse('https://www.zarinpal.com/pg/StartPay/' + result.Authority)
    else:
        return HttpResponse('Error')


def verify(request):
    client = Client(ZARINPAL_WEBSERVICE)
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MMERCHANT_ID,
                                                    request.args['Authority'],
                                                    amount)
        if result.Status == 100:
            return HttpResponse('Transaction success. RefID: ' + str(result.RefID))
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed. Status: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')


def gateway(request):
    return render(request, 'gateway.html', {})
