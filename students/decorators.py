from .models import json_data,studentsList
from django.urls import reverse
import datetime
import json



def addmonth(function):
    def wrap(request,id):
        stu=studentsList.objects.get(id=id)
        try:
            student=json_data.objects.get(student=stu)
        except:
            student=json_data.objects.create(student=stu)
            student.save()
            return function(request,id)
        mydate = datetime.datetime.now()
        key=mydate.strftime("%B") # 'December'
        s=student.data
        data=eval(s)
        data[key][1]+=1
        student.data=data
        student.save()
        return function(request,id)
    return wrap


def admin_or_refer(function):
    def wrap(request,id):
        stu=studentsList.objects.get(id=id)
        if request.is_authenticate() is not True:
            return reverse('report', kwargs={'student':stu})

        return function(request,id)
    return wrap