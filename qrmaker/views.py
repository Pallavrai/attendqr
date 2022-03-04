from datetime import date, datetime
from django.shortcuts import render,HttpResponse,redirect,reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from students.models import attendon,studentsList
from datetime import date
import datetime
import qrcode
from django.urls import resolve
from students.models import attendon
from django.utils import timezone
from students.decorators import addmonth, admin_or_refer

def generate(request,id):
    curl=request.META['HTTP_HOST']
    img = qrcode.make(curl+'/mark/'+str(id))
    #img.save("some_file.png")
    
    response = HttpResponse(content_type="image/jpeg")
    img.save(response, "JPEG")
    return response

@admin_or_refer
@addmonth
def markattendance(request,id):
    try:
        stu=studentsList.objects.get(id=id)
        uid=str(f'{id}-{datetime.datetime.now().strftime("%y%m%d")}')
        atten=attendon.objects.create(udate=uid,student=stu,attended=True)
        atten.save()
    except:
        return JsonResponse({'success':'False'})
    return JsonResponse({'success':'True'})
