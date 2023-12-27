from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Contact

def index(request):
    old_cname = "Max Smith"; 
    new_cname = "John Doe"; 
    x = Contact.objects.filter(contact_name='Max Smith')[0]
    cname = x.contact_name
    if cname==old_cname:
       x.contact_name = new_cname
       x.save()
    context = {
        'cname' : new_cname
    }
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context,request))


