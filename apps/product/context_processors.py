from .models import SiteSettings

def site_settings(request):
    try:
        settings = SiteSettings.objects.first()
    except:
        settings = None
    return {'site_settings': settings}

def cart_data(request):
    cart = request.session.get('cart', {})
    total_price = 0
    total_quantity = 0
    for item in cart.values():
        total_price +=  item['price']*item['quantity']
        total_quantity += item['quantity']
    return {
        'cart_items': cart,
        'cart_total_price': total_price,
        'cart_total_quantity': total_quantity,
    }