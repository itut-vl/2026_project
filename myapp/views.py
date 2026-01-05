from django.http import JsonResponse, HttpResponse
import json
from django.shortcuts import render
from .models import Item


def dashbord_open(request):
    return render(request, 'dashbord.html')

def item_register_open(request):
    return render(request, 'item_register.html')

def order_list_open(request):
    return render(request, 'order_list.html')

def shipping_list_open(request):
    return render(request, 'shipping_list.html')

def ajax_save_item(request):
    if request.method =='POST':
        
        item_no = request.POST.get('item_no')
        item_name = request.POST.get('item_name')
        item_price = request.POST.get('item_price')
        delivery_date = request.POST.get('delivery_date')
        
        Item.objects.create(
            item_no = item_no,
            item_name = item_name,
            item_price = item_price,
            delivery_date=delivery_date
        )
        return JsonResponse({'status': 'success', 'message': '成功'})

    return JsonResponse({'status': 'error', 'message': '失敗'})