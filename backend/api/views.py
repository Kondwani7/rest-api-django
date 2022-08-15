#get views 
import json
from django.http import JsonResponse, HttpResponse
from products.models import Product
from django.forms.models import model_to_dict
#api views
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    #get model data
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['title', 'price'])
    return Response(data)
