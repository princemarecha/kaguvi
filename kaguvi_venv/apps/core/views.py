from django.shortcuts import render
from apps.product.models import Product
# Create your views here.
def frontpage(request):
    newest_product = Product.objects.all()[0:8]

    value = request.user.is_anonymous
    if value == True :
        context = {
            'newest_product': newest_product,
            'anonymous':value
        }

    elif value == False:
        recommended = Product.objects.filter(car=request.user.customer.car, model=request.user.customer.model,engine=request.user.customer.engine)[0:8]
        context = {
            'newest_product': newest_product,
            'recommended': recommended,
            'anonymous': value
        }

    return render(request, 'core/front_page.html', context) #newest_products to show newer products on front page.

def contact(request):
    return render(request, 'core/contact.html')