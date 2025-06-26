from django.shortcuts import redirect, render,HttpResponse,get_object_or_404
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
    roles = role.objects.all()
    departments = Department.objects.all()
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
        return render(request, 'add_employee.html', {
        'form_title': 'Add New Employee',
        'roles': roles,
        'departments': departments
        })
def delete_employee(request,emp_id=0):
    if emp_id:
        emp_del = Employee.objects.get(id=emp_id)
        emp_del.delete()
        return redirect('home')
    

def update_employee(request, emp_id):
    employee = get_object_or_404(Employee, id=emp_id)

    departments = Department.objects.all()
    roles = role.objects.all()
    blood_groups = Employee.blood_c  # Your blood group choices tuple

    if request.method == 'POST':
        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.phone = int(request.POST.get('phone', 0))
        employee.salary = int(request.POST.get('salary', 0))
        hire_date_str = request.POST.get('hire_date')
        if hire_date_str:
            employee.hire_date = datetime.strptime(hire_date_str, '%Y-%m-%d').date()
        employee.blood_group = request.POST.get('blood_group')

        dept_id = request.POST.get('dept')
        position_id = request.POST.get('Position')

        employee.dept = Department.objects.get(id=dept_id) if dept_id else None
        employee.Position = role.objects.get(id=position_id) if position_id else None

        employee.save()
        return redirect('home')

    return render(request, 'update_employee.html', {
        'employee': employee,
        'departments': departments,
        'roles': roles,
        'blood_groups': blood_groups,
        'title': 'Update Employee'
    })
