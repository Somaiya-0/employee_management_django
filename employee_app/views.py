from django.shortcuts import redirect, render,HttpResponse
from .models import Department,role,Employee
from datetime import date

# Create your views here.
def home(request):
    emps = Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'index.html',context)


def add_employee(request):
    if request.method == 'POST':
        name= request.POST['name']
        email=  request.POST['email']
        Position= int(request.POST['Position'])
        dept= int(request.POST['dept'])
        blood_group= request.POST['blood_group']
        salary= int(request.POST['salary'])
        phone= int(request.POST['phone'])

        employee= Employee(name=name, email=email, Position_id = Position, dept_id=dept, blood_group=blood_group, salary= salary, hire_date=date.today(), phone=phone)
        employee.save()
        return redirect('home')
    elif request.method=='GET':
        print("get")
        
        return render(request,'add_employee.html')

def delete_employee(request,emp_id=0):
    if emp_id:
        emp_del = Employee.objects.get(id=emp_id)
        emp_del.delete()
        return redirect('home')

    #return render(request,'index.html')

def update_employee(request,emp_id):
    if emp_id:
        emp_update= Employee.objects.get(id=emp_id)
    return render(request,'update_employee.html')