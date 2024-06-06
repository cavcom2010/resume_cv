from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import path
from .forms import ContactForm
from django.core.mail import send_mail
from .models import ProgrammingLanguage, Testimonial

# Create your views here.
def index(request):
    """This view contains all the the language and the form models"""
    """and the main index.html file or homepage."""
    language = ProgrammingLanguage.objects.all()
    testimonials = Testimonial.objects.order_by('-date')
    context = {
        'form': ContactForm,
        'language': language,
        'testimonials': testimonials,

    }
    return render(request, 'index.html', context)

def contact(request):
    """this is a simple form for people to contact the site admin."""
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

def add_testimonial(request):
    """a view to render the function to add a new testimonial."""
    pass








