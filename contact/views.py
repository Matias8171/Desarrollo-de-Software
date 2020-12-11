
from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data = request.POST)
        # Validaciones
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            message = request.POST.get('message','')
        # Email

            email = EmailMessage(
                "RRPMP: Nuevo Mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name,email,message),
                "no-contestar@inbox.mailtrap.io",
                ["matias.treupil@gmail.com"],
                reply_to=[email]
            )

            try:
                email.send()
                return redirect(reverse('contact') + "?aceptado")   
            except:
                return redirect(reverse('contact') + "?rechazado")   


    return render(request,"contact/contact.html",{'form':contact_form})