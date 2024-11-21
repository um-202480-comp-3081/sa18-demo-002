from django.shortcuts import render, get_object_or_404
from .models import Customer


# Create your views here.
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, "app/customer_list.html", {"customers": customers})


def customer_detail(request, id):
    customer = get_object_or_404(Customer, id=id)
    return render(request, "app/customer_detail.html", {"customer": customer})
