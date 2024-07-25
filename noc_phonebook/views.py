from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import department_tbl
# Create your views here.

def vdepartment(request):
    departments=department_tbl.objects.all().values()
    template=loader.get_template('all_department.html')
    context={
        'departments':departments,
    }
    return HttpResponse(template.render(context, request))

def vdepartment_detail(request, id):
    des=department_tbl.objects.get(id=id)
    template = loader.get_template('department_detail.html')
    context ={
        'des':des,
    }
    return HttpResponse(template.render(context, request))

def vmain(request):
    departments=department_tbl.objects.all().values()
    template=loader.get_template('all_department.html')
    context={
        'departments':departments,
    }
    return HttpResponse(template.render(context, request))