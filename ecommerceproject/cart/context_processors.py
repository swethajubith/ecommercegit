from.models import  Cart,CartItem
from.views import _cartid
def counter(request):
   itemcount=0
   if 'admin' in request.path:
      return {}
   else:
     try:
        cart=Cart.objects.filter(cartid=_cartid(request))
        cartitems=CartItem.objects.all().filter(cart=cart[:1])
        for cartitem in cartitems:
            itemcount += cartitem.quantity
     except Cart.DoesNotExist:
        itemcount=0
   return dict(itemcount=itemcount)
