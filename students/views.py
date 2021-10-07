from django.shortcuts import render
from students.models import studentsList,attendon
from django.utils import timezone

def home(request):
    return render(request,'home.html')

def list_students(request,section=None):
    stu=studentsList.objects.all().order_by('name')

    for s in stu:
        if attendon.objects.filter(student=s,date=timezone.now()).exists():
                stu=studentsList.objects.exclude(name=s.name).all()

    for s in stu:
        # if attendon.objects.filter(student=s,date=timezone.now()).exists():
        #     stu=studentsList.objects.exclude(name=s.name).all()
        if section:
            stu=studentsList.objects.filter(section=section)
        if request.GET.get('name',False):
            nm=request.GET.get('name',False)
            stu=studentsList.objects.filter(name__contains=nm)
        if section and request.GET.get('name',False):
            nm=request.GET.get('name',False)
            stu=studentsList.objects.filter(section=section,name__contains=nm)


    
    context={
        'Students':stu
    }

    return render(request,'list_students.html',context)

