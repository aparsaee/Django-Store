from django.shortcuts import render

# Create your views here.


def gateway(request):
    return render(request, 'gateway.html', {})
