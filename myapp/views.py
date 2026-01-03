from django.shortcuts import render

def dashbord_open(request):
    return render(request, 'dashbord.html')

def item_register_open(request):
    return render(request, 'item_register.html')

def order_list_open(request):
    return render(request, 'order_list.html')

def shipping_list_open(request):
    return render(request, 'shipping_list.html')