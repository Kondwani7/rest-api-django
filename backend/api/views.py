#get views 
import json
from django.http import JsonResponse

from products.models import Product

def api_home(request, *args, **kwargs):
    #get model data
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data['title'] = model_data.title
        data['description'] = model_data.description
        data['price'] = model_data.price
    return JsonResponse(data)
