from email.policy import default
from statistics import mode
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

    name=models.CharField(null=False,max_length=255)
    email=models.EmailField(null=True)
    parent_name=models.CharField(max_length=255)
    standard=models.IntegerField()
    phone=models.BigIntegerField(null=True)
    section=models.CharField(max_length=6,choices=section_names)
    rollno=models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        super(studentsList, self).save(*args, **kwargs)
        student=json_data.objects.create(student=self)
        student.save()


class attendon(models.Model):
    student=models.ForeignKey(studentsList,on_delete=models.CASCADE)
    date=models.DateField(default=timezone.now)
    attended=models.BooleanField(default=False)


    def __str__(self):
        return str(self.student)    

class json_data(models.Model):
    student=models.ForeignKey(studentsList,on_delete=models.CASCADE)
    data=models.TextField(default={
                                    "January":0,
                                    "February":0,
                                    "March":0,
                                    "April":0,
                                    "May" :0,
                                    "June" :0,
                                    "July":0,
                                    "August":0,
                                    "September":0,
                                    "October":0,
                                    "November":0,
                                    "December":0
                                    })
   

    def __str__(self):
        return str(self.student)
t=datetime.datetime.now()
# def get_data(year):
#     try:
#         data=year_range.objects.get(year=year)
#     except:
#         data=year_range.object.create(year=year,range_data={
#                                     "January":31,
#                                     "February":28,
#                                     "March":31,
#                                     "April":30,
#                                     "May" :31,
#                                     "June" :30,
#                                     "July":31,
#                                     "August":31,
#                                     "September":30,
#                                     "October":31,
#                                     "November":30,
#                                     "December":31
#     })
#         data.save()
    
#     finally:
#         return year_range.objects.get(year=year).range_data



class year_range(models.Model):
    year=models.IntegerField(default=t.year,primary_key=True)
    range_data=models.TextField(default={
                                    "January":31,
                                    "February":28,
                                    "March":31,
                                    "April":30,
                                    "May" :31,
                                    "June" :30,
                                    "July":31,
                                    "August":31,
                                    "September":30,
                                    "October":31,
                                    "November":30,
                                    "December":31
    })

    def __str__(self):
        return str(self.year)