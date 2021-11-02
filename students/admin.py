from django.contrib import admin
from students.models import *

class StudentAdmin(admin.ModelAdmin):
    list_display=('name','standard','section')
    list_filter = ('standard','section')
    search_fields=['name']

class AttendonAdmin(admin.ModelAdmin):
    list_filter = ('attended','date')
    search_fields=['student']

class AttendmonthAdmin(admin.ModelAdmin):
    search_fields = ['student']
    list_filter = ('name','days')

admin.site.register(studentsList,StudentAdmin)
admin.site.register(attendMonth,AttendmonthAdmin)
admin.site.register(attendon,AttendonAdmin)
# Register your models here.
