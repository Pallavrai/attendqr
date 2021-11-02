from django.db import models
from django.shortcuts import HttpResponse
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.db.models.query_utils import select_related_descend
import datetime
from django.utils import timezone

from django.http.response import HttpResponse
class studentsList(models.Model):
    section_names=[
        ('A','science'),
        ('C','commerce'),
        ('H','humanity')]

    name=models.CharField(null=False,max_length=20)
    standard=models.IntegerField()
    section=models.CharField(max_length=6,choices=section_names)
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
    udate=models.TextField(primary_key=True)
    student=models.ForeignKey(studentsList,on_delete=models.CASCADE)
    #month=models.
    date=models.DateField(default=timezone.now)
    attended=models.BooleanField(default=False)


    def __str__(self):
        return str(self.student)    

    
    # def delete(self,*args,**kwargs):
    #     mydate = datetime.datetime.now()
    #     name_month=mydate.strftime("%B")
    #     month=attendMonth.objects.get(student=self.student,name=name_month)
    #     month.days=month.days-1
    #     month.save()
    #     super().delete(*args,**kwargs)


    def save(self,*args,**kwargs):
            
            # uid=str(f'{self.student_id}-{timezone.now().strftime("%y%m%d")}')
            # s=attendon.objects.get(student=self.student,udate=uid)
            # s.save()
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
                
            super().save(*args,**kwargs)
