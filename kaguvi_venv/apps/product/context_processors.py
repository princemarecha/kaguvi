#global functionality (mainly to process categories)

from apps.product.models import Category

def menu_categories(request):
    categories = Category.objects.all()

    return {'menu_categories': categories}
