from django.shortcuts import render
from django.http import JsonResponse
import os, sys
from datetime import datetime


def main(request):
    print(dir(request))
    return render(request, 'main.html', {'parameter': "test"})


def health(request):
    current_page = request.get_host() + request.get_full_path()
    response = {
        'date': datetime.now(), 
        'current_page': current_page, 
        'server_info': {'platform': sys.platform}, 
        'client_info': os.getlogin()
    }
    return JsonResponse(response)