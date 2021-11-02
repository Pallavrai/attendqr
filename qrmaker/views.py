from datetime import date, datetime
from django.shortcuts import render,HttpResponse,redirect,reverse
from django.contrib.auth.decorators import login_required
from students.models import attendon,studentsList
from datetime import date
import datetime
import qrcode
from django.urls import resolve
from students.models import attendMonth,attendon
from django.utils import timezone
def generate(request,id):
    curl=request.META['HTTP_HOST']
    img = qrcode.make(curl+'/mark/'+str(id))
    #img.save("some_file.png")
    
    response = HttpResponse(content_type="image/jpeg")
    img.save(response, "JPEG")
    return response

@login_required
def markattendance(request,id):
    stu=studentsList.objects.get(id=id)
    uid=str(f'{id}-{timezone.now().strftime("%y%m%d")}')
    atten=attendon.objects.create(udate=uid,student=stu,attended=True)
    atten.save()
    # mydate = datetime.datetime.now()
    # name_month=mydate.strftime("%B")
    # try:
    #     month=attendMonth.objects.get(student=stu)
    #     month.name=name_month
    #     if self.attended:
    #         month.days=month.days+1
    # except:
    #     month=attendMonth.objects.create(student=stu,name=name_month)
    # month.save()

    return redirect(reverse('list_students'))
