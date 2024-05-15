from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Emp(models.Model):  # Renamed from Employee to Emp
    name = models.CharField(max_length=200)
    emp_id = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    supervisor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    hire_date = models.DateField(auto_now=False, auto_now_add=True)
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class PerformanceEvaluation(models.Model):
    employee = models.ForeignKey(Emp, on_delete=models.CASCADE)  # Changed from Employee to Emp
    evaluation_date = models.DateField()
    performance_rating = models.IntegerField()
    comments = models.TextField()

class Payroll(models.Model):
    employee = models.ForeignKey(Emp, on_delete=models.CASCADE)  # Changed from Employee to Emp
    pay_period_start_date = models.DateField()
    pay_period_end_date = models.DateField()
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)
    overtime_hours = models.DecimalField(max_digits=5, decimal_places=2)
    gross_pay = models.DecimalField(max_digits=10, decimal_places=2)
    deductions = models.DecimalField(max_digits=10, decimal_places=2)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2)
