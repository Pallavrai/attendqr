from .models import json_data,studentsList
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

