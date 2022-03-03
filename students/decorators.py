from .models import json_data,studentsList
from django.urls import reverse
from django.shortcuts import redirect
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
        data[key]+=1
        student.data=data
        student.save()
        return function(request,id)
    return wrap


def admin_or_refer(function):
    def wrap(request,id):
        if request.user.is_authenticated is not True:
            return redirect(reverse('report', args=[id]))

        return function(request,id)
    return wrap