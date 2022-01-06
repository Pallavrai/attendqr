from django.shortcuts import render
from students.models import studentsList,attendon
from django.utils import timezone

def home(request):
    return render(request,'home.html')

def list_students(request,section='A'):
    usrs=list(attendon.objects.filter(date=timezone.now()).values_list('student', flat=True))
    nm=''
    if request.GET.get('name'):
        nm=request.GET.get('name')
    stu=studentsList.objects.exclude(pk__in=usrs).filter(section__exact=section,name__icontains=nm).order_by('name')
    
    context={
        'Students':stu
    }

    return render(request,'list_students.html',context)

def student_report(request,student):
    return render(request,'student_report.html')

