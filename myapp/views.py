from django.http import JsonResponse, HttpResponse
import json
from django.shortcuts import render
from .models import Item


def dashbord_open(request):
    return render(request, 'dashbord.html')



def order_list_open(request):
    return render(request, 'order_list.html')

def shipping_list_open(request):
    return render(request, 'shipping_list.html')

def ajax_save_item(request):
    if request.method =='POST':
        
        item_no = request.POST.get('item_no')
        item_name = request.POST.get('item_name')
        item_price = request.POST.get('item_price')

        if Item.objects.filter(item_no=item_no).exists():
            return JsonResponse({'status': 'error_duplicate', 'message': item_no})
        
        Item.objects.create(
            item_no = item_no,
            item_name = item_name,
            item_price = item_price,
        )
        return JsonResponse({'status': 'success', 'message': item_no})

    return JsonResponse({'status': 'error', 'message': item_no})

def ajax_delete_item(request):
    if request.method =='POST':

        item_no = request.POST.get('item_no')

        if not Item.objects.filter(item_no=item_no).exists():
            return JsonResponse({'status':'error_nai', 'message': item_no})
        
        Item.objects.filter(item_no=item_no).delete()
        
        return JsonResponse({'status': 'success', 'message': item_no})
            
    return JsonResponse({'status': 'error', 'message': item_no})

def item_register_open(request):
    items = Item.objects.all() 
    return render(request, 'item_register.html', {'items': items})