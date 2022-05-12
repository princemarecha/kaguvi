from django.contrib import admin

# Register your models here.
from .models import Vendor, vendorProfile

admin.site.register(Vendor) #model registering
admin.site.register(vendorProfile) #model registering