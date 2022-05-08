from io import BytesIO                          #to manipulate data
from PIL import Image

from django.core.files import File
from django.db import models

from apps.vendor.models import Vendor

# Create your models here.
class Category(models.Model): # a class for product categories
    title = models.CharField(max_length=255)
    slug =  models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordering'] #order by ordering field

    def __str__(self):
        return self.title #string represantation of the category

class Product (models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE) #related_name to get all products in category, on delete to delete all products in category
    vendor = models.ForeignKey(Vendor, related_name='products',on_delete=models.CASCADE)  # related_name to get all products to vendor, on delete to delete all products of vendor
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price  = models.DecimalField(max_digits=6, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    car = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    engine =  models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ['-date_added']              #orders products by newest products first

    def __str__(self):
        return self.title  # string represantation of the product

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:                               #if user did upload any picture, use placeholder
                return 'https://via.placeholder.com/240x180.jpg'

    def make_thumbnail(self, image, size=(300,200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return  thumbnail
