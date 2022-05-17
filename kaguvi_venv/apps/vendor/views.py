from django.contrib.auth import  login #for user login operation
from django.contrib.auth.decorators import login_required #so that users can log in and out (gui)
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm #use default user creation form
from django.utils.text import slugify #to slugify the title
# Create your views here.
from apps.product.models import Product
#import our database model
from .models import Vendor
from .forms import ProductForm, vendorProfile

#view to create vendor
def become_vendor(request):
    if request.method == 'POST': #if the form is not yet submitted it will be GET
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save() #user created if form is valid

            login(request, user) #this user is logged in

            vendor = Vendor.objects.create(name=user.username, created_by=user) #vendor creation based on the newly created user

            return redirect('your_location')
    else:
            form = UserCreationForm #leave it blank so that we don't parse any infomation in there

    return render(request, 'vendor/become_vendor.html', {'form':form}) #add form as context to use it in the front end

@login_required #checks if user is logged in first before proceeding, or he will be redirected to the login page
def vendor_admin(request):
    v_account = False

    vendors = Vendor.objects.all()
    for ven in vendors:
        if ven.name == request.user.username:
            v_account = True

    if v_account == True:
        vendor = request.user.vendor #vendor which belongs to this user
        products = vendor.products.all()
        orders = vendor.orders.all()

        for order in orders:
            order.vendor_amount = 0
            order.vendor_paid_amount = 0
            order.fully_paid = True

            for item in order.items.all():
                if item.vendor == request.user.vendor:
                    if item.vendor_paid:
                        order.vendor_paid_amount += item.get_total_price()

                    else:
                        order.vendor_amount += item.get_total_price()
                        order.fully_paid = False
    elif v_account == False:
        return redirect("login")


    return render(request, 'vendor/vendor_admin.html',{'vendor': vendor, 'products':products,'orders':orders})

@login_required
def add_product(request):
    if request.method == 'POST':  # if the form is not yet submitted it will be GET
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product =  form.save(commit=False) # because we havent stated the vendor yet, otherwise it will crash
            product.vendor = request.user.vendor
            product.slug = slugify(product.title)
            product.save()

            return redirect('vendor_admin')
    else:
            form = ProductForm()

    return render(request, 'vendor/add_product.html', {'form': form})

@login_required
def edit_vendor(request):
    vendor = request.user.vendor

    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')

        if name:
            vendor.created_by.email = email
            vendor.created_by.save()

            vendor.name = name
            vendor.save()

            return redirect('vendor_admin')

    return render(request, 'vendor/edit_vendor.html', {'vendor': vendor})

def vendors(request):
    vendors = Vendor.objects.all()

    return render(request, 'vendor/vendors.html', {'vendors': vendors})

def vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id) #Vendor model and its primary key for detailed view of vendor
    return render(request, 'vendor/vendor.html', {'vendor': vendor})

def vendor_profile(request):

    form = vendorProfile(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('frontpage')

    form = vendorProfile()
    context = {
        'form':form
    }
    return render(request, 'vendor/vendor_profile.html', context)

