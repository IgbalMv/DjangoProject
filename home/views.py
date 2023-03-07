from django.shortcuts import render
from django.http import (   HttpResponse,
                            JsonResponse)


def index(request):
    return render(request, 'index.html')


def contact(request):

    return render(template_name='contact.html',request=request)

