from django.shortcuts import render

from django.http import HttpResponse
import datetime
from .models import Product
from django.views import generic

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def  product_list(request):
    context={'key':'value','products':Product.objects.all()}
    return render(request, 'product_list.html', context)


