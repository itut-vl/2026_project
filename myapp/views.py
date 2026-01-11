from django.http import JsonResponse, HttpResponse
import json
from django.shortcuts import render
from .models import Item
from django.views import View


def dashbord_open(request):
    return render(request, 'dashbord.html')

def shipping_list_open(request):
    return render(request, 'shipping_list.html')

def item_register_open(request):
    return render(request, 'item_register.html')


class Item_register(View):
    def get(self, request):
        return render(request, 'item_register.html')

    def post(self, request):
        if request.POST.get("kubun") == "save_item":
            return self.save_item(request)
        if request.POST.get("kubun") == "delete_item":
            return self.delete_item(request)
        if request.POST.get("kubun") == "get_item":
            return self.get_item(request)

    def save_item(self, request):
        import json
        fields = json.loads(request.POST.get('fields'))
        print(fields)
        

        items = Item(**fields)
        print(items)

        if Item.objects.filter(item_no=items.item_no).exists():
           return JsonResponse({'status': 'error_duplicate', 'message': items.item_no})
        
        items.save()

        return JsonResponse({'status': 'success', 'message': items.item_no})

    def delete_item(self, request):
        import json
        fields = json.loads(request.POST.get('fields'))

        item_no = fields['item_no']

        if not Item.objects.filter(item_no=item_no).exists():
            return JsonResponse({'status':'error_nai', 'message': item_no})
        
        Item.objects.filter(item_no=item_no).delete()
        
        return JsonResponse({'status': 'success', 'message': item_no})
        

    def get_item(self, request):
        items = list(Item.objects.all().values())
        return JsonResponse({'data': items})


class Order_input(View):
    def get(self, request):
        return render(request, 'order_input.html')

    def post(self, request):
        if request.POST.get("kubun") == "get_item":
            return self.get_item(request)
        
    def get_item(self, request):
        items = list(Item.objects.all().values())
        return JsonResponse({"items": items})
