from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
# Create your views here.
def store(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_totals':0}

    context = {'Product':products,'order':order}
    return render(request,'store/store.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_totals':0}
    context = {'items':items,'order':order}
    return render(request,'store/checkout.html',context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_totals':0}
    context = {'items':items,'order':order}
    return render(request,'store/cart.html',context)
def updateitem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items,created = OrderItem.objects.get_or_create(order=order,product=product)
    if action=="add":
        items.quantity = items.quantity + 1
    elif action=="remove":
        items.quantity = items.quantity-1
    items.save()
    if items.quantity<=0:
        items.delete()
    return  JsonResponse("Item was added",safe=False)
