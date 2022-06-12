from django.shortcuts import render, redirect
from apps.product.models import Product
from apps.vendor.models import Vendor
from apps.customers.models import Customer
# Create your views here.
def frontpage(request):


    v_account = False
    vendors = Vendor.objects.all()
    for ven in vendors:
        print(ven.name)
        if ven.name == request.user.username:
            v_account = True
            try:
                print(ven.vendorprofile.latitude)
            except:
                user = request.user
                user.delete()
                return redirect('frontpage')




    newest_product = Product.objects.all()[0:8]

    value = request.user.is_anonymous

    if value == True or (v_account == True and (request.user.customer.all().count() == 0) ) :
        context = {
            'newest_product': newest_product,
            'anonymous':value,
            'vendors': vendors
        }

    elif value == False or (v_account == True and (request.user.customer.all().count() != 0) ):
        c_profile = request.user.customer.all()
        cnt = request.user.customer.all().count()
        counting = 0
        recommended = []
        for cust in c_profile:
            recommended.extend(Product.objects.filter(car=cust.car, model=cust.model,engine=cust.engine)[0:8])

            context = {
                'c_profile':c_profile,
                'newest_product': newest_product,
                'recommended': recommended,
                'anonymous': value,
                'vendors': vendors,
                'counting':counting,
                'v_account':v_account,
                'cnt':cnt
            }
            counting = counting + 1

    return render(request, 'core/front_page.html', context) #newest_products to show newer products on front page.

def contact(request):

    return render(request, 'core/contact.html')
def about(request):

    return render(request, 'core/about.html')

def delete_car(request, car_id):
    car = Customer.objects.get(pk=car_id)
    car.delete()

    return redirect('frontpage')
