import json

from django.shortcuts import render, HttpResponse
from .models import NCRdelhiBoys
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def test_endpoint(request):
    return HttpResponse("Ping Pong")

def get_all_users(request):
    if request.method=='GET':
        a=NCRdelhiBoys.objects.all()
        new_d = []
        new_fic = {}
        for i in a:
            new_fic['name']=i.user_name
            new_fic['phone']=i.contact_num
            new_fic['created_date']=str(i.created_date)
            new_d.append(new_fic.copy())
        return HttpResponse(json.dumps(new_d, indent=2))
    else:
        return HttpResponse("nothing")

@csrf_exempt
def add_users(request):
    if request.method == 'POST':
        name = request.GET.get('user_name')
        contact_num = request.GET.get('contact_num')
        save_obj = NCRdelhiBoys(user_name=name, contact_num=contact_num)
        save_obj.full_clean()
        save_obj.save()
        if save_obj:
            return HttpResponse('Success')
        else:
            return HttpResponse('Failure')






