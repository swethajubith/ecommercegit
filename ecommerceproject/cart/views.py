
from django.shortcuts import render,redirect
from.models import Cart,CartItem
from ecommerceapp.models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
def _cartid(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def addcart(request,productid):
    product=Product.objects.get(id=productid)
    try:
        cart=Cart.objects.get(cartid=_cartid(request))

    except Cart.DoesNotExist:
        cart=Cart.objects.create(cartid=_cartid(request))
        cart.save()
    try:
        cartitem=CartItem.objects.get(product=product,cart=cart)
        if cartitem.quantity < cartitem.product.stock:
             cartitem.quantity += 1
        cartitem.save()

    except CartItem.DoesNotExist:
            cartitem=CartItem.objects.create(product=product,quantity=1,cart=cart)
            cartitem.save()

    return redirect('cart:cartdetail')
    # return render(request,'product.html')
def cartdetail(request,total=0,counter=0,cartitems=None):
     try:
         cart=Cart.objects.get(cartid=_cartid(request))
         cartitems=CartItem.objects.filter(cart=cart,active=True)
         for cartitem in cartitems:
             total += (cartitem.product.price * cartitem.quantity)
             counter += cartitem.quantity

     except ObjectDoesNotExist:
         pass
     return render(request,'cart.html',dict(cartitems=cartitems,total=total,counter=counter))
def cartremove(request,productid):
    cart=Cart.objects.get(cartid=_cartid(request))
    product=get_object_or_404(Product,id=productid)
    cartitem=CartItem.objects.get(product=product,cart=cart)
    if cartitem.quantity > 1:
        cartitem.quantity -=1
        cartitem.save()
    else:
        cartitem.delete()
    return redirect('cart:cartdetail')
def fullremove(request,productid):
    cart=Cart.objects.get(cartid=_cartid(request))
    product=get_object_or_404(Product,id=productid)
    cartitem=CartItem.objects.get(product=product, cart=cart)
    cartitem.delete()
    return redirect('cart:cartdetail')