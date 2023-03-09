from django.shortcuts import render
from home.models import Contact
from django.http import (   HttpResponse,
                            JsonResponse)


def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        messages = request.POST.get('messages')
        Contact.objects.create(name = name, email = email, subject = subject, messages = messages)

    return render(template_name='contact.html', request=request)

