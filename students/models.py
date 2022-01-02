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

    def save(self,*args,**kwargs):
        super(studentsList, self).save(*args, **kwargs)
        student=json_data.objects.create(student=self)
        student.save()


class attendon(models.Model):
    udate=models.TextField(primary_key=True)
    student=models.ForeignKey(studentsList,on_delete=models.CASCADE)
    date=models.DateField(default=timezone.now)
    attended=models.BooleanField(default=False)


    def __str__(self):
        return str(self.student)    

class json_data(models.Model):
    student=models.ForeignKey(studentsList,on_delete=models.CASCADE)
    data=models.TextField(default={
                                    "January":[31,0],
                                    "February":[28,0,29],
                                    "March":[31,0],
                                    "April":[30,0],
                                    "May" :[31,0],
                                    "June" :[30,0],
                                    "July":[31,0],
                                    "August":[31,0],
                                    "September":[30,0],
                                    "October":[31,0],
                                    "November":[30,0],
                                    "December":[31,0]
                                    })
   

    def __str__(self):
        return str(self.student)