from django.shortcuts import render

from django.http import HttpResponse
import datetime
from .models import Product

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

# def product_list(request):
#     text="""
#         <ul>
#     """
#     for i in Product.objects.all():
#         text = text+'<li>'+str( i )+'</li>'
#     return HttpResponse(text)


def  product_list(request):
    context={'key':'value'}
    return render(request, 'product_list.html', context)
