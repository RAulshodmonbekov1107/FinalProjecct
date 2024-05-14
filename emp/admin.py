from django.contrib import admin
from .models import Department, Emp, PerformanceEvaluation, Payroll

# Register your models here.
admin.site.register(Department)
admin.site.register(Emp)
admin.site.register(PerformanceEvaluation)
admin.site.register(Payroll)
