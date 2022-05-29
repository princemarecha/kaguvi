from django.shortcuts import render
from apps.product.models import Product
from apps.vendor.models import Vendor
# Create your views here.
def frontpage(request):

    v_account = False
    vendors = Vendor.objects.all()
    for ven in vendors:
        if ven.name == request.user.username:
            v_account = True

    newest_product = Product.objects.all()[0:8]


    value = request.user.is_anonymous
    if value == True or v_account == True :
        context = {
            'newest_product': newest_product,
            'anonymous':value,
            'vendors': vendors
        }

    elif value == False or v_account == False:
        c_profile = request.user.customer.all()
        recommended = []
        for cust in c_profile:
            recommended.extend(Product.objects.filter(car=cust.car, model=cust.model,engine=cust.engine)[0:8])
            context = {
                'c_profile':c_profile,
                'newest_product': newest_product,
                'recommended': recommended,
                'anonymous': value,
                'vendors': vendors
            }

    return render(request, 'core/front_page.html', context) #newest_products to show newer products on front page.

def contact(request):
    return render(request, 'core/contact.html')