from django.contrib.auth.models import User #for user authorisation
from django.db import models

# Create your models here. (database tables)
class Vendor(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True) #auto capture date of upload
    created_by = models.OneToOneField(User, related_name='vendor', on_delete = models.CASCADE) #one to one rltship, 1 user has one instance of this table, and user deletes defaults to vendor delete(on_delete)

    class Meta:
        ordering = ['name'] # now ordering of this model will be by name not default id

    def __str__(self): #returns name of the object rather than the whole object, string represantation
        return self.name

    def get_balance(self):
        items = self.items.filter(vendor_paid = False, order__vendor__in=[self.id]) #all unpaid items
        return sum((item.product.price * item.quantity) for item in items)

    def get_paid_amount(self):
        items = self.items.filter(vendor_paid=True, order__vendor__in=[self.id])  # all unpaid items
        return sum((item.product.price * item.quantity) for item in items)

