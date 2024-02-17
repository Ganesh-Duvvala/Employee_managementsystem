from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def emp_home(request):
    emps = emp.objects.all()

    return render(request,'home.html',{"emps":emps})
def add_emp(request):
    if request.method =="POST":
        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_add = request.POST.get("emp_add")
        emp_ws = request.POST.get("emp_ws")
        emp_dpt = request.POST.get("emp_dpt")
        e = emp()
        e.name = emp_name
        e.empId = emp_id
        e.Phone = emp_phone 
        e.address = emp_add
        if emp_ws is None:
            e.working = False
        else:
            e.working = True
        e.department = emp_dpt
        e.save()
        print("data is comming")
        return redirect("/emp/home/")
    return render(request,'add_emp.html')
def delete_emp(request,emp_id):
    emp_del=emp.objects.get(pk = emp_id)
    emp_del.delete()
    return redirect("/emp/home/")

def update_emp(request,emp_id):
    emp_update=emp.objects.get(pk = emp_id)
    return render(request,"update_emp.html",{"emp":emp_update})
def do_update(request,emp_id):
    if request.method == "POST":
        emp_name = request.POST.get("emp_name")
        emp_Id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_add = request.POST.get("emp_add")
        emp_ws = request.POST.get("emp_ws")
        emp_dpt = request.POST.get("emp_dpt")
        e=emp.objects.get(pk = emp_id)
        e.name = emp_name
        e.empId = emp_Id
        e.Phone = emp_phone 
        e.address = emp_add
        if emp_ws is None:
            e.working = False
        else:
            e.working = True
        e.department = emp_dpt
        e.save()
    return redirect("/emp/home/")
