from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import path
from .forms import ContactForm
from django.core.mail import send_mail
from .models import ProgrammingLanguage

# Create your views here.
def index(request):
    language = ProgrammingLanguage.objects.all()
    return render(request, 'index.html',{'form':ContactForm, 'language':language })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                subject=f"Message from {full_name.title()} at email {email}.",
                message = message,
                from_email = 'calvin2411@hotmail.com',
                recipient_list=['calvin2411@hotmail.com', 'calvin2411@yahoo.co.uk'],
                fail_silently=False, 
            )
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form':form})







