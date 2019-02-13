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

class ProductListView(generic.ListView):
    model = Product
    template_name = 'product_list2.html'
    #queryset = Product.objects.filter(category='V')
    queryset = Product.objects.all()
    # paginate_by = 3
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['name'] = 'Hey Wasit!!'
        
        return context

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Hey Wasit!!'
        return context

