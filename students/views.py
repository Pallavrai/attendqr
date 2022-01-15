from django.shortcuts import render
from students.models import studentsList,attendon,json_data
from django.utils import timezone
import datetime as dt

def home(request):
    return render(request,'home.html')

def list_students(request,section='A'):
    usrs=list(attendon.objects.filter(date=timezone.now()).values_list('student', flat=True))
    nm=''
    if request.GET.get('name'):
        nm=request.GET.get('name')
    stu=studentsList.objects.exclude(pk__in=usrs).filter(section__exact=section,name__icontains=nm).order_by('name')
    if request.user.is_authenticated is not True:
        stu=studentsList.objects.filter(section__exact=section,name__icontains=nm).order_by('name')
    context={
        'Students':stu
    }

    return render(request,'list_students.html',context)

def student_report(request,student):
    student=studentsList.objects.get(id=student)
    try:
        t=dt.date.today()
        atndon=attendon.objects.get(student=student,date=t)
        obj_attendon="Present"
        
    except attendon.DoesNotExist:
        obj_attendon="Absent"
    context={
        'attendon':obj_attendon,
        'student':student,
        'jsondata':json_data
    }
    return render(request,'student_report.html',context)

