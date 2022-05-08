from django.contrib.auth import  login #for user login operation
from django.contrib.auth.decorators import login_required #so that users can log in and out (gui)
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm #use default user creation form
from django.utils.text import slugify #to slugify the title
from django.contrib.auth.models import User
from .forms import CustomerProfile

from .models import Customer
# Create your views here.


def profile_create_view(request):

    form = CustomerProfile(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('frontpage')

    form = CustomerProfile()
    context = {
        'form':form
    }
    return render(request, 'customer/customer.html', context)

def become_customer(request):
    if request.method == 'POST': #if the form is not yet submitted it will be GET
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save() #user created if form is valid
            login(request, user) #this user is logged in
            customer = Customer.objects.create(name=user.username) #vendor creation based on the newly created user
            return redirect('your_car')
    else:
            form = UserCreationForm #leave it blank so that we don't parse any infomation in there

    return render(request, 'customer/become_customer.html', {'form':form}) #add form as context to use it in the front end



