from django.shortcuts import render
from .models import *

# Create your views here.
def products_list(request):
    prdcts = Product.objects.all()
    return render(
        request,
        'products.html',
        {'products': prdcts}
    )