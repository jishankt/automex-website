from django.shortcuts import render
from .models import Client, Testimonial

def client_list(request):
    clients = Client.objects.filter(is_active=True).order_by('order')
    testimonials = Testimonial.objects.filter(is_approved=True, is_featured=True)
    
    context = {
        'clients': clients,
        'testimonials': testimonials,
    }
    return render(request, 'clients/client_list.html', context)