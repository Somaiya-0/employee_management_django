from django.shortcuts import redirect, render
from .models import Department,role,Employee

# Create your views here.
def home(request):
    emps = Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'index.html',context)


def add_employee(request):
    if request.method == 'POST':
        print('y')
    else:
        print('n')
    return render(request,'add_employee.html')

def delete_employee(request,id):
    return render(request,'index.html')

def update_employee(request,id):
    return render(request,'update_employee.html')