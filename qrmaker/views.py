from datetime import date, datetime
from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from students.models import attendon,studentsList
from datetime import date
import qrcode

def generate(request,id):
    img = qrcode.make(id)
    type(img)
    #img.save("some_file.png")
    
    response = HttpResponse(content_type="image/jpeg")
    img.save(response, "JPEG")
    return response

@login_required
def markattendance(request,id):
    stu=studentsList.objects.get(id=id)
    atten=attendon.objects.create(student=stu,attended=True)
    atten.save()
    return HttpResponse('Submited')
