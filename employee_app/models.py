from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=150,null=True)

    def __str__(self):
        return self.name

class role(models.Model):
    name=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    blood_c=(
        ('1','A+')
        ,('2','B+')
        ,('3','O+'),
        ('4','A-')
        ,('5','B-')
        ,('6','C-')
        ,('7','O-')
        ,('8','AB+')
        ,('9','AB-')     
    )
    name=models.CharField(max_length=150,null=True)
    blood_group=models.CharField(max_length=3,choices=blood_c)
    dept=models.ForeignKey(Department, on_delete=models.CASCADE)
    Position=models.ForeignKey(role, on_delete=models.CASCADE)
    phone=models.CharField(max_length=150)
    email=models.CharField(max_length=400,null=True)
    salary=models.IntegerField(default=0)
    hire_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return "%s %s %s %s %s %s %s %s " %(self.name, self.get_blood_group_display(),self.dept,self.Position, self.phone, self.email, self.salary, self.hire_date)