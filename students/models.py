from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.db.models.query_utils import select_related_descend
import datetime
class studentsList(models.Model):
    name=models.CharField(null=False,max_length=20)
    standard=models.IntegerField()
    section=models.CharField(max_length=10)
    rollno=models.IntegerField(default=0)

    def __str__(self):
        return self.name
class attendMonth(models.Model):
    student=models.ForeignKey(studentsList,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    days=models.IntegerField(default=1)

    def __str__(self):
        return f'{self.name} - {str(self.student)}'

class attendon(models.Model):
    student=models.ForeignKey(studentsList,on_delete=models.CASCADE)
    #month=models.ForeignKey(attendMonth,on_delete=models.CASCADE)
    date=models.DateField()
    attended=models.BooleanField(default=False)

    def __str__(self):
        return str(self.student)

    def save(self,*args,**kwargs):
        
        mydate = datetime.datetime.now()
        name_month=mydate.strftime("%B")
        try:
            month=attendMonth.objects.get(student=self.student)
            month.name=name_month
            if self.attended:
                month.days=month.days+1
        except:
            month=attendMonth.objects.create(student=self.student,name=name_month)
        

       

        month.save()

        return super().save(*args,**kwargs)
