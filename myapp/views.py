from django.shortcuts import render
from .models import Item
import json
from django.http import JsonResponse 


def dashbord_open(request):
    return render(request, 'dashbord.html')

def item_register_open(request):
    return render(request, 'item_register.html')

def order_list_open(request):
    return render(request, 'order_list.html')

def shipping_list_open(request):
    return render(request, 'shipping_list.html')

def ajax_save_item(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            Item.objects.create(
                item_no = data.get('item_no'),
                item_name = data.get('item_name'),
                item_price = data.get('item_price'),
                delivery_date = data.get('delivery_date')
            )
            
            return JsonResponse({'status': 'ok'})
            
        except Exception as e:
            # デバッグ用：エラー内容を表示
            print("エラー発生:", e)
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status':  'error','message': "POSTじゃない"})