from django.http import JsonResponse
from django.shortcuts import render
from students.models import studentsList,attendon
from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def sms_home(request):
    usrs=list(attendon.objects.filter(date=timezone.now()).values_list('student', flat=True))
    students=studentsList.objects.exclude(pk__in=usrs)

    context={
        'students':students
    }

    return render(request,'sms.html',context)

def send(request,lst_students):
    return JsonResponse
