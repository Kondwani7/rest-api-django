#get views 
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    return JsonResponse({"message": "Your first view with a Api built in Django"})
