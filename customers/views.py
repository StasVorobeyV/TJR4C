from django.shortcuts import render
from .models import Customer

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/templates/customer_list.html', {'customers': customers})

def customer_detail(request, pk):
    customer = Customer.objects.get(pk=pk)
    return render(request, 'customers/templates/customer_detail.html', {'customer': customer})
