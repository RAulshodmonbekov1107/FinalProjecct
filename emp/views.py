from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Emp, Department


def emp_home(request):
    emps=Emp.objects.all()
    return render(request,"emp/home.html",{'emps':emps})


def add_emp(request):
    if request.method=="POST":
        print(request.POST)
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")
        emp_salary=request.POST.get("emp_salary")
        e=Emp()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.salary=emp_salary
        e.department=Department.objects.get_or_create(name = emp_department)[0]
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()
        return redirect("/emp/home/")
    return render(request,"emp/add_emp.html",{})

def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/home/")

def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    print("Yes Bhai")
    return render(request,"emp/update_emp.html",{
        'emp':emp
    })

def do_update_emp(request,emp_id):
    if request.method=="POST":
        emp_name=request.POST.get("emp_name")
        emp_id_temp=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")

        e=Emp.objects.get(pk=emp_id)

        e.name=emp_name
        e.emp_id=emp_id_temp
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()
    return redirect("/emp/home/")

# views.py

from django.shortcuts import render, redirect
from .forms import PerformanceEvaluationForm
from .models import PerformanceEvaluation

def create_performance_evaluation(request):
    if request.method == 'POST':
        form = PerformanceEvaluationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_performance_evaluations')  # Replace this with your actual URL name
    else:
        form = PerformanceEvaluationForm()

    return render(request, 'perform/create_performance_evaluation.html', {'form': form})

# views.py

def list_performance_evaluations(request):
    evaluations = PerformanceEvaluation.objects.all()
    return render(request, 'perform/list_performance_evaluations.html', {'evaluations': evaluations})

# views.py

from django.shortcuts import render, redirect
from .forms import PayrollForm

def add_payroll(request):
    if request.method == 'POST':
        form = PayrollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payroll_list')  # Replace this with your actual URL name for payroll listings
    else:
        form = PayrollForm()

    return render(request, 'payroll/add_payroll.html', {'form': form})
# views.py


from .models import Payroll

def payroll_list(request):
    payrolls = Payroll.objects.all()
    return render(request, 'payroll/payroll_list.html', {'payrolls': payrolls})
