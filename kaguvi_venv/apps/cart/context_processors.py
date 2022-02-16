from .cart import Cart

def cart(request):
    return {'cart': Cart(request)} #make this globally available to every template in project