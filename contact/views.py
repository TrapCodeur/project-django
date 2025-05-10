from django.shortcuts import render, redirect
from contact.models import Contact
# Create your views here.

def contact(request):
    contacts = Contact.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        com = Contact(name=name, email=email, message=message)
        com.save()
        return redirect("confirmation")

    return render(request, "accounts\\contact.html")

def confirmation_view(request):
    return render(request, "accounts\\confirmation.html")