from django.shortcuts import render
from apps.product.models import Product
# Create your views here.
def frontpage(request):
    newest_product = Product.objects.all()[0:8]

    return render(request, 'core/front_page.html', {'newest_product': newest_product}) #newest_products to show newer products on front page.

def contact(request):
    return render(request, 'core/contact.html')